from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from drafter.models import League, User, FantasyTeam, Message
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

"""
Team related views
"""
def team_roster(request, league_id, user_id):
    team = FantasyTeam.objects.get(league_id=league_id, manager=user_id)
    league = League.objects.get(id=league_id)
    data = {
        'team': team, 'league': league, 'league_id': league_id
    }
    return render(request, 'drafter/leagues/details/team/roster.html', data)
"""
Team schedule
"""
def team_schedule(request, league_id=None, user_id=None):
    team = FantasyTeam.objects.get(league_id=league_id, manager=user_id)
    league = League.objects.get(id=league_id)
    data = {
        'team' : team, 'league': league, 'league_id': league_id
    }
    return render(request, 'drafter/leagues/details/team/schedule.html', data)
"""
Team transactions
"""
def team_transactions(request, league_id=None, user_id=None):
    team = FantasyTeam.objects.get(league_id=league_id, manager=user_id)
    league = League.objects.get(id=league_id)
    data = {
        'team': team, 'league': league, 'league_id': league_id
    }
    return render(request, 'drafter/leagues/details/team/transactions.html', data)
"""
Team draft picks
"""
def team_picks(request, league_id=None, user_id=None):
    team = FantasyTeam.objects.get(league_id=league_id, manager=user_id)
    league = League.objects.get(id=league_id)
    data = {
        'team': team, 'league':league, 'league_id': league_id

    }
    return render(request, 'drafter/leagues/details/team/picks.html', data)
"""
Team settings
"""
@login_required
def team_settings(request, league_id=None, user_id=None):
    team = FantasyTeam.objects.get(league_id=league_id, manager=user_id)
    league = League.objects.get(id=league_id)
    data = {
        'team': team, 'league': league, " league_id": league_id
    }
    return render(request, 'drafter/leagues/details/team/settings.html', data)

"""
Create a FantasyTeam with given league and user
"""
@login_required
def create_team(request, league_id=None, user_id=None):
    # If the request is a POST we hit the DB and do access checks
    if request.method == 'POST':
        league = League.objects.get(id=league_id)
        # Create a team if there is no team associated with the given (league_id, user_id)
        # and the requesting user is either the league's commish or the given user
        if FantasyTeam.objects.filter(manager=user_id, league=league_id).count() == 0 and \
                (request.user.id == int(user_id) or request.user == league.commish):
            FantasyTeam.objects.create(manager=User.objects.get(id=user_id), league=league)
            try:
                join_request = Message.objects.get(target_league=league, sender=user_id)
                return redirect(reverse('delete_request', kwargs={ 'request_id': join_request.id }))
            except Message.DoesNotExist:
                pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def delete_team(request, league_id=None, user_id=None):
    if request.method == 'POST':
        league = League.objects.get(id=league_id)
        # Try to get a team associated with the user and league
        try:
            team = FantasyTeam.objects.get(league=league, manager=user_id)
        except FantasyTeam.DoesNotExist:
            team = None
        # Delete the FantasyTeam object if the requester is the user or the league commish and the team exists
        if request.user.id == int(user_id) or request.user == league.commish and team is not None:
            team.delete()
    return redirect(reverse('league', kwargs={ 'league_id': league_id }))
