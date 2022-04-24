import graphene
from graphene_django.debug import DjangoDebug
from apps.rooms.mutations import CreateRoom, WriteTurn
from apps.rooms.types import RoomType, RoundType
from apps.rooms.models import Room, Turn, Round
from apps.organizations.models import Organization
from graphene_subscriptions.events import CREATED, UPDATED, DELETED
from apps.rooms.tasks import MONTH_EVENT


class Query(graphene.ObjectType):
    debug_rooms = graphene.Field(
        DjangoDebug, name='__debug_rooms')
    room_by_code = graphene.Field(
        RoomType, code=graphene.String(), description='Информация о комнате по коду комнаты')
    rooms_in_organization = graphene.List(
        RoomType, subdomain=graphene.String(), description='Список комнат в организации')
    can_do_step_now_by_code = graphene.Boolean(code=graphene.String())
    current_round_by_code = graphene.Field(
        RoundType, code=graphene.String(), description='Информация о текущем раунде по коду комнаты')

    def resolve_can_do_step_now_by_code(root, info, code):
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
                turn = Turn.objects.filter(
                    month=current_month, user=user).count()
                return turn == 0
            else:
                raise Exception('Error code')
        except Exception as e:
            return None

    def resolve_rooms_in_organization(root, info, subdomain):
        try:
            organization = Organization.objects.get(subdomain=subdomain)
            return Room.objects.filter(organization=organization).order_by('-key')
        except Exception as e:
            return None

    def resolve_room_by_code(room, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)
                return room
            else:
                raise Exception('Error code')
        except Exception as e:
            return None

    def resolve_current_round_by_code(self, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)
                return room.current_round
        except Exception as e:
            return None


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    write_turn = WriteTurn.Field()


def filter_room_events(event, room):
    try:
        if (event.operation == UPDATED):
            return (isinstance(event.instance, Room) and event.instance.pk == int(room.id))
        # elif event.operation == MONTH_EVENT:
        #     if (isinstance(event.instance, Room)):
        #         if (event.instance.id == int(room.id)):
        #             return True
        #     elif int(event.instance['id']) == int(room.id):
        #         event.instance = room
        #         return True
        #     else:
        #         return False
        else:
            return False
    except Exception as e:
        return False


def filter_round_events(event, current_round):
    try:
        if (event.operation == UPDATED):
            return (event.operation == UPDATED and isinstance(event.instance, Round) and event.instance.pk == int(current_round.id))
        else:
            return False
    except Exception as e:
        return False


class Subscription(graphene.ObjectType):
    room_updated = graphene.Field(RoomType, code=graphene.String())
    current_round_updated = graphene.Field(RoundType, code=graphene.String())

    # Подписка на обновления комнаты по коду
    def resolve_room_updated(self, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                user = info.context.user
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)
                print(room.current_round.current_month)
                print(room.current_round.current_month.key)
                return self.filter(lambda event: filter_room_events(event, room)).map(lambda event: event.instance)

            else:
                raise Exception('Error code')
        except Exception as e:
            return None

    # Подписка на обновление текущего раунда комнаты
    def resolve_current_round_updated(self, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                user = info.context.user
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)
                current_round = room.current_round
                print(room.current_round.current_month)
                print(room.current_round.current_month.key)
                return self.filter(lambda event: filter_round_events(event, current_round)).map(lambda event: event.instance)
        except Exception as e:
            return None
