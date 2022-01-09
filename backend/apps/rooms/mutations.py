import graphene
from apps.rooms.models import Room, Round, Month
from organizations.models import Organization
from apps.users.models import User
from apps.rooms.types import RoundType


class CreateRoom(graphene.Mutation):
    """ Мутация для создания комнаты (+ раунда и необходимого количества месяцев) в пространстве организации """
    room_id = graphene.ID()
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    code = graphene.String()
    round = graphene.Field(RoundType)

    class Arguments:
        subdomain = graphene.String(required=True)
        user_id = graphene.ID(required=True)
        number_of_turns = graphene.Int(required=True)
        money_per_month = graphene.Int(required=True)

    def mutate(self, info, subdomain, user_id, number_of_turns, money_per_month):
        try:
            organization = Organization.objects.get(subdomain=subdomain)
            user = User.objects.get(pk=user_id)

            # Создаём новый объект комнаты
            room = Room.objects.create(
                organization=organization, room_owner=user, number_of_turns=number_of_turns, money_per_month=money_per_month)
            code = str(room)

            # Создаём новый раунд в комнате
            round = Round.objects.create(room=room)

            # Создаём необходимое количество месяцев
            for _ in range(room.number_of_turns):
                Month.objects.create(round=round)

            return CreateRoom(success=True, room_id=room.id, code=code, round=round)
        except Exception as e:
            return CreateRoom(success=False, errors=[str(e)])
