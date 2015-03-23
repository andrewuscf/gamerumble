from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from drafter.models import League, User, FantasyTeam, Message
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@login_required
def new_join_requests(request, league_id=None):
    league = League.objects.get(id=league_id)
    if league.commish == request.user:
        requests = Message.objects.filter(request=True, target_league=league_id, new=True)
        return render(request, 'drafter/leagues/details/settings/requests.html', { 'league_id': league_id, 'league': league, 'requests': requests })
    else:
        return redirect(reverse('drafter.views.league', kwargs={ 'league_id': league_id }))
    
@login_required
def create_request(request, league_id=None):
    if request.method == 'POST':
        league = League.objects.get(id=league_id)
        if league.users.count() >= league.size:
            return redirect(reverse('drafter.views.league', kwargs={ 'league_id': league_id }))
        if league.public:
            return redirect(reverse('drafter.views.league', kwargs={ 'league_id': league_id }))
        else:
            # If the league is private, send a join request
            Message.objects.create(sender=User.objects.get(id=request.user.id), recipient=league.commish, target_league=league, request=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def delete_request(request, request_id=None):
    join_request = Message.objects.get(id=request_id)
    if request.user == join_request.recipient:
        join_request.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
