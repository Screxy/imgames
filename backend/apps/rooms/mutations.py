import graphene
from .models import Room, Round, Month, Turn, CardChoice, RoomParticipant

from apps.organizations.models import Organization
from apps.flows.models import Flow, Card
from apps.users.models import User
from .types import RoundType, RoomType, TurnType


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
            first_month = None
            for _ in range(room.number_of_turns+1):
                print(_)
                if first_month is not None:
                    Month.objects.create(round=round)
                else:
                    first_month = Month.objects.create(round=round)

            round.current_month = first_month
            round.save()

            # Добавляем пользователя как участника
            RoomParticipant.objects.create(room=room, user=user)

            return CreateRoom(success=True, room=room, code=code, round=round)
        except Exception as e:
            return CreateRoom(success=False, errors=[str(e)])


class WriteTurn(graphene.Mutation):
    """ Мутация для создания комнаты (+ раунда и необходимого количества месяцев) в пространстве организации """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    turn = graphene.Field(TurnType)

    class Arguments:
        code = graphene.String(required=True)
        cards_id = graphene.List(graphene.ID, required=True)

    def mutate(self, info, code, cards_id):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                user = info.context.user
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)
                current_round = room.current_round
                current_month = current_round.current_month

                # Если шаг существует, возвращаем ошибку
                turn = Turn.objects.filter(
                    month=current_month, user=user).count()
                if turn != 0:
                    raise Exception('Turn exists!')

                # Если не сущестовал такой ход, тогда создаём
                turn = Turn.objects.create(
                    month=current_month, user=user)

                # Для каждой карточки фиксируем выбор
                for card_id in cards_id:
                    card = Card.objects.get(pk=card_id)
                    CardChoice.objects.create(card=card, turn=turn)

                # Возвращаем результат
                return WriteTurn(turn=turn, success=True)
            return WriteTurn(success=False, errors=['Error code!'])
        except Exception as e:
            return WriteTurn(success=False, errors=[str(e)])
