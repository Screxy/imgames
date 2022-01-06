from django.contrib import admin
from .models import Winner, Turn, Month, Round, Room, RoomParticipant


@admin.register(RoomParticipant)
class RoomParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room')
    list_display_links = ('id', 'user')


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
    readonly_fields = ('key',)


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'room', 'current_month',
                    'is_active', 'created_at')
    readonly_fields = ('key', 'created_at', 'updated_at')
    search_fields = ('room__organization__prefix',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'organization', 'room_owner',
                    'number_of_turns', 'current_round')
    list_filter = ('organization',)
    readonly_fields = ('key',)
