from views import *

__author__ = 'Andrew'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # list generic urls
    url(r'^api/teams/$', TeamGenericListAPIView.as_view(), name="api_teams"),
    url(r'^api/players/$', PlayerGenericListAPIView.as_view(), name="api_players"),
    url(r'^api/users/$', UserGenericListAPIView.as_view(), name="api_users"),
    url(r'^api/leagues/$', UserGenericListAPIView.as_view(), name="api_leagues"),
    url(r'^api/messages/$', MessageGenericListAPIView.as_view(), name="api_messages"),
    url(r'^api/fantasyteams/$', FantasyTeamGenericListAPIView.as_view(), name="api_fantasyteams"),
    url(r'^api/fantasycontracts/$', FantasyContractGenericListAPIView.as_view(), name="api_fantasycontracts"),
    url(r'^api/fantasymatchs/$', FantasyMatchGenericListAPIView.as_view(), name="api_fantasymatchs"),
    url(r'^api/connectiontickets/$', ConnectionTicketGenericListAPIView.as_view(), name="api_connectiontickets"),

    # Retrieve urls
    url(r'^api/teams/(?P<pk>[0-9]+)/$', TeamDetail.as_view(), name="api_team"),
    url(r'^api/players/(?P<pk>[0-9]+)/$', PlayerDetail.as_view(), name="api_player"),
    url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name="api_user"),
    url(r'^api/leagues/(?P<pk>[0-9]+)/$', LeagueDetail.as_view(), name="api_league"),
    url(r'^api/messages/(?P<pk>[0-9]+)/$', MessageDetail.as_view(), name="api_message"),
    url(r'^api/fantasyteams/(?P<pk>[0-9]+)/$', FantasyTeamDetail.as_view(), name="api_fantasyteam"),
    url(r'^api/fantasycontracts/(?P<pk>[0-9]+)/$', FantasyContractDetail.as_view(), name="api_fantasycontract"),
    url(r'^api/fantasymatchs/(?P<pk>[0-9]+)/$', FantasyMatchDetail.as_view(), name="api_fantasymatch"),
    url(r'^api/connectiontickets/(?P<pk>[0-9]+)/$', ConnectionTicketDetail.as_view(), name="api_connectionticket"),


    # create urls
    url(r'^api/teams/create/$', TeamCreate.as_view(), name="api_team"),
    url(r'^api/players/create/$', PlayerCreate.as_view(), name="api_player"),
    url(r'^api/users/create/$', UserCreate.as_view(), name="api_user"),
    url(r'^api/leagues/create/$', LeagueCreate.as_view(), name="api_league"),
    url(r'^api/messages/create/$', MessageCreate.as_view(), name="api_message"),
    url(r'^api/fantasyteams/create/$', FantasyTeamCreate.as_view(), name="api_fantasyteam"),
    url(r'^api/fantasycontracts/create/$', FantasyContractCreate.as_view(), name="api_fantasycontract"),
    url(r'^api/fantasymatchs/create/$', FantasyMatchCreate.as_view(), name="api_fantasymatch"),
    url(r'^api/connectiontickets/create/$', ConnectionTicketCreate.as_view(), name="api_connectionticket"),
)
