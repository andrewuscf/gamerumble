from django.conf.urls import *
from drafter import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    
    # User URLs
    url(r'^register/$', views.new_user, name='new_user'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<user_id>\d+)/$', views.user, name='user'),
    url(r'^users/(?P<username>[\w.@+-]+)/$', views.user, name='user'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'drafter/index.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/' }, name='logout'),
    
    # League URLs
    url(r'^leagues/$', views.leagues, name='leagues'),
    url(r'^leagues/new/$', views.new_league, name='new_league'),
    url(r'^leagues/(?P<league_id>\d+)/$', views.league, name='league'),
    url(r'^leagues/(?P<league_id>\d+)/standings/$', views.league_standings, name='league_standings'),
    url(r'^leagues/(?P<league_id>\d+)/draft/$', views.league_draft, name='league_draft'),
    url(r'^leagues/(?P<league_id>\d+)/rosters/$', views.league_rosters, name='league_rosters'),
    url(r'^leagues/(?P<league_id>\d+)/scoring/$', views.league_scoring, name='league_scoring'),
    url(r'^leagues/(?P<league_id>\d+)/playoffs/$', views.league_playoffs, name='league_playoffs'),
    url(r'^leagues/(?P<league_id>\d+)/schedule/$', views.league_schedule, name='league_schedule'),
    
    # Commish settings URLs
    url(r'^leagues/(?P<league_id>\d+)/settings/$', views.league_settings, name='league_settings'),
    url(r'^leagues/(?P<league_id>\d+)/settings/requests$', views.new_join_requests, name='new_join_requests'),
    url(r'^leagues/(?P<league_id>\d+)/settings/draft$', views.league_draft_settings, name='league_draft_settings'),
    
    # Request URLS
    url(r'^leagues/(?P<league_id>\d+)/join/$', views.create_request, name='create_request'),
    url(r'^requests/(?P<request_id>\d+)/del$', views.delete_request, name='delete_request'),
    
    # FantasyTeam URLs, user-league management
    url(r'^leagues/(?P<league_id>\d+)/add/(?P<user_id>\d+)$', views.create_team, name='create_team'),
    url(r'^leagues/(?P<league_id>\d+)/del/(?P<user_id>\d+)$', views.delete_team, name='delete_team'),
    url(r'^leagues/(?P<league_id>\d+)/(?P<user_id>\d+)/roster$', views.team_roster, name='team_roaster'),
    url(r'^leagues/(?P<league_id>\d+)/(?P<user_id>\d+)/schedule$', views.team_schedule, name='team_schedule'),
    url(r'^leagues/(?P<league_id>\d+)/(?P<user_id>\d+)/transactions$', views.team_transactions,
        name='team_transactions'),
    url(r'^leagues/(?P<league_id>\d+)/(?P<user_id>\d+)/picks$', views.team_picks, name='team_picks'),
    url(r'^leagues/(?P<league_id>\d+)/(?P<user_id>\d+)/settings$', views.team_settings, name='team_settings'),
)