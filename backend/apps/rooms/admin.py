from django.contrib import admin
from .models import Winner, Turn, Month, Round, Room


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('place', 'user',  'round')
    list_display_links = ('place', 'user',)


@admin.register(Turn)
class TurnAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'month')


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'round', 'counter')


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'room', 'current_month')
    readonly_fields = ('key',)
    search_fields = ('room__organization__prefix',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'organization', 'room_owner',
                    'number_of_turns', 'current_round')
    list_filter = ('organization',)
    readonly_fields = ('key',)
