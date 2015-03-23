from django.contrib import admin
from explorer.models import *
from drafter.models import *


class LeagueAdmin(admin.ModelAdmin):
    pass

admin.site.register(League, LeagueAdmin)
admin.site.register(Team, LeagueAdmin)
admin.site.register(FantasyTeam, LeagueAdmin)
admin.site.register(Player, LeagueAdmin)
admin.site.register(RawGameData, LeagueAdmin)
admin.site.register(RawPlayerData, LeagueAdmin)