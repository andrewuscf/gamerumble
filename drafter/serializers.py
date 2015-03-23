from rest_framework import serializers
from drafter.models import User, Team, Player, League, Message, FantasyTeam, FantasyContract, FantasyMatch, \
    ConnectionTicket

__author__ = 'Andrew'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Player
        fields = ('team', 'name', 'region')



class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam


class FantasyContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyContract


class FantasyMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyMatch


class ConnectionTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionTicket