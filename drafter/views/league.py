from django.shortcuts import render, redirect
from drafter.forms import LeagueCreationForm, LeagueEditForm, BaseDraftOrderFormSet
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from drafter.models import League, FantasyTeam, ConnectionTicket
from django.core.urlresolvers import reverse

"""
League-related views
"""
"""
View all leagues
"""


def leagues(request):
    all_leagues = list(League.objects.all())
    if request.user.is_authenticated():
        my_leagues = list(request.user.leagues.all())
        commish_leagues = list(request.user.managed_leagues.all())
    else:
        my_leagues = None
        commish_leagues = None

    data = { 'all_leagues': all_leagues, 'my_leagues': my_leagues, 'commish_leagues': commish_leagues }
    return render(request, 'drafter/leagues/leagues.html', data)

"""
Create a new league
"""
@login_required
def new_league(request):
    if request.method == 'POST': # If the form was submitted...
        form = LeagueCreationForm(request.POST) # Make a form bound to the POST data
        if form.is_valid():
            new_league = form.save(commit=False)
            new_league.commish = request.user
            new_league.save()
            FantasyTeam.objects.create(manager=request.user, league=new_league)
            return redirect(reverse('league', kwargs={ 'league_id': new_league.id }))
    else:
        form = LeagueCreationForm() # Unbound form
    return render(request, 'drafter/leagues/new.html', { 'form': form })



"""
View a league's standings
"""


def league_standings(request, league_id=None):
    league = League.objects.get(id=league_id)
    teams = [(a+1, b) for (a, b) in enumerate(league.teams.all().order_by('wins'))]
    data = {
        'league_id': league_id, 'league': league, 'teams': teams
    }
    return render(request, 'drafter/leagues/details/league/standings.html', data)

"""
View a league's rosters
"""


def league_rosters(request, league_id):
    league = League.objects.get(id=league_id)
    data = {
        'league_id': league_id, 'league': league
    }
    return render(request, 'drafter/leagues/details/league/rosters.html', data)
    
"""
View a league's scoring rules
"""


def league_scoring(request, league_id=None):
    league = League.objects.get(id=league_id)
    data = {
        'league_id': league_id, 'league': league
    }
    return render(request, 'drafter/leagues/details/league/scoring.html', data)
"""
View a league's playoff bracket
"""


def league_playoffs(request, league_id=None):
    league = League.objects.get(id=league_id)
    data ={
        'league_id': league_id, 'league': league
    }
    return render(request, 'drafter/leagues/details/league/playoffs.html', data)

"""
View a league's schedule
"""

def league_schedule(request, league_id=None):
    league = League.objects.get(id=league_id)
    data = {
        'league_id': league_id, 'league': league
    }
    return render(request, 'drafter/leagues/details/league/schedule.html', data)
    
"""
View a league's draft management page
"""
@login_required
def league_draft(request, league_id=None):
    league = League.objects.get(id=league_id)
    if league in request.user.leagues.all() or league.commish == request.user:
        # Get Session
        sessionid = request.COOKIES.get('sessionid')
        # Create connection ticket, one per user
        try:
            ticket = ConnectionTicket.objects.get(user=request.user)
            ticket.delete()
        except ConnectionTicket.DoesNotExist:
            ticket = None
        
        ticket = ConnectionTicket.objects.create(user=request.user, user_sessionid=sessionid)
        # Send this back to the user?
        
        return render(request, 'drafter/leagues/details/league/draft.html', { 'league_id': league_id, 'league': league })
    else:
        return redirect(reverse('drafter.views.league', kwargs={ 'league_id': league_id }))


@login_required
def league_settings(request, league_id=None):
    league = League.objects.get(id=league_id)
    if league.commish == request.user:
        success = False
        if request.method == 'POST':
            form = LeagueEditForm(request.POST, instance=league)
            if form.is_valid():
                form.save()
                success = True
        else:
            form = LeagueEditForm(instance=league) 
        return render(request, 'drafter/leagues/details/settings/settings.html', { 'league_id': league_id, 'league': league, 'form': form, 'success': success })
    else:
        return redirect(reverse('league', kwargs={'league_id': league_id}))


@login_required
def league_draft_settings(request, league_id=None):
    league = League.objects.get(id=league_id)
    if league.commish == request.user:
        success = False
        DraftOrderFormSet = modelformset_factory(FantasyTeam, fields=("draft_pick", ), formset=BaseDraftOrderFormSet, max_num=league.teams.count(), extra=0)
        if request.method == 'POST':
            formset = DraftOrderFormSet(request.POST, queryset=FantasyTeam.objects.filter(league=league))
            if formset.is_valid():
                formset.save()
                success = True
        else:
            formset = DraftOrderFormSet(queryset=FantasyTeam.objects.filter(league=league))
        return render(request, 'drafter/leagues/details/settings/draft.html', { 'league_id': league_id, 'league': league, 'formset': formset, 'success': success })
    else:
        return redirect(reverse('drafter.views.league', kwargs={ 'league_id': league_id }))


def league(request, league_id=None):
    return redirect(reverse('league_standings', kwargs={'league_id': league_id}))