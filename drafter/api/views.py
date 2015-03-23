from rest_framework import generics
from drafter.models import Team, Player, User, League, Message, FantasyTeam, FantasyContract, FantasyMatch, \
    ConnectionTicket
from drafter.serializers import TeamSerializer, PlayerSerializer, UserSerializer, ConnectionTicketSerializer, \
    FantasyMatchSerializer, FantasyContractSerializer, MessageSerializer, FantasyTeamSerializer, LeagueSerializer
#
# list APIVIEW


class TeamGenericListAPIView(generics.ListAPIView):
    model = Team
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return Team.objects.all()


class PlayerGenericListAPIView(generics.ListAPIView):
    model = Player
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get_queryset(self):
        return Player.objects.all()


class UserGenericListAPIView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()


class LeagueGenericListAPIView(generics.ListAPIView):
    model = League
    serializer_class = LeagueSerializer
    queryset = League.objects.all()

    def get_queryset(self):
        return League.objects.all()


class MessageGenericListAPIView(generics.ListAPIView):
    model = Message
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        return Message.objects.all()


class FantasyTeamGenericListAPIView(generics.ListAPIView):
    model = FantasyTeam
    serializer_class = FantasyTeamSerializer
    queryset = FantasyTeam.objects.all()

    def get_queryset(self):
        return FantasyTeam.objects.all()


class FantasyContractGenericListAPIView(generics.ListAPIView):
    model = FantasyContract
    serializer_class = FantasyContractSerializer
    queryset = FantasyContract.objects.all()

    def get_queryset(self):
        return FantasyContract.objects.all()


class FantasyMatchGenericListAPIView(generics.ListAPIView):
    model = FantasyMatch
    serializer_class = FantasyMatchSerializer
    queryset = FantasyMatch.objects.all()

    def get_queryset(self):
        return FantasyMatch.objects.all()


class ConnectionTicketGenericListAPIView(generics.ListAPIView):
    model = ConnectionTicket
    serializer_class = ConnectionTicketSerializer
    queryset = ConnectionTicket.objects.all()

    def get_queryset(self):
        return ConnectionTicket.objects.all()


# Generic CreateAPIView

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class FantasyTeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer


class FantasyContractDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FantasyContract.objects.all()
    serializer_class = FantasyContractSerializer


class FantasyMatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FantasyMatch.objects.all()
    serializer_class = FantasyMatchSerializer


class ConnectionTicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConnectionTicket.objects.all()
    serializer_class = ConnectionTicketSerializer


# create views

class TeamCreate(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerCreate(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LeagueCreate(generics.CreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class MessageCreate(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class FantasyTeamCreate(generics.CreateAPIView):
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer


class FantasyContractCreate(generics.CreateAPIView):
    queryset = FantasyContract.objects.all()
    serializer_class = FantasyContractSerializer


class FantasyMatchCreate(generics.CreateAPIView):
    queryset = FantasyMatch.objects.all()
    serializer_class = FantasyMatchSerializer


class ConnectionTicketCreate(generics.CreateAPIView):
    queryset = ConnectionTicket.objects.all()
    serializer_class = ConnectionTicketSerializer
