from .models import RoomParticipant, CardChoice, Winner, Turn, Month, Round, Room
from graphene_django.types import DjangoObjectType


class RoomParticipantType(DjangoObjectType):
    class Meta:
        model = RoomParticipant
        fields = "__all__"


class CardChoiceType(DjangoObjectType):
    class Meta:
        model = CardChoice
        fields = "__all__"


class WinnerType(DjangoObjectType):
    class Meta:
        model = Winner
        fields = "__all__"


class TurnType(DjangoObjectType):
    class Meta:
        model = Turn
        fields = "__all__"


class MonthType(DjangoObjectType):
    class Meta:
        model = Month
        fields = "__all__"


class RoundType(DjangoObjectType):
    class Meta:
        model = Round
        fields = "__all__"


class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = "__all__"
