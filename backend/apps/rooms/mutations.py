import graphene
from apps.rooms.models import Room, Round, Month, RoomParticipant
from organizations.models import Organization
from apps.flows.models import Flow
from apps.users.models import User
from apps.rooms.types import RoundType, RoomType


class CreateRoom(graphene.Mutation):
    """ Мутация для создания комнаты (+ раунда и необходимого количества месяцев) в пространстве организации """
    room = graphene.Field(RoomType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    code = graphene.String()
    round = graphene.Field(RoundType)

    class Arguments:
        subdomain = graphene.String(required=True)
        number_of_turns = graphene.Int(required=True)
        money_per_month = graphene.Int(required=True)
        flow_id = graphene.ID(required=True)

    def mutate(self, info, subdomain, number_of_turns, money_per_month, flow_id):
        try:
            organization = Organization.objects.get(subdomain=subdomain)
            user = info.context.user

            # Находим механику
            flow = Flow.objects.get(pk=flow_id)

            # Создаём новый объект комнаты
            room = Room.objects.create(
                organization=organization, room_owner=user, number_of_turns=number_of_turns, money_per_month=money_per_month, flow=flow)
            code = str(room)

            # Создаём новый раунд в комнате
            round = Round.objects.create(room=room)
            room.current_round = round
            room.save()

            # Создаём необходимое количество месяцев
            for _ in range(room.number_of_turns):
                Month.objects.create(round=round)

            # Добавляем пользователя как участника
            RoomParticipant.objects.create(room=room, user=user)

            return CreateRoom(success=True, room=room, code=code, round=round)
        except Exception as e:
            return CreateRoom(success=False, errors=[str(e)])
