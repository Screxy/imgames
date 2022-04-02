import graphene
from graphene_django.debug import DjangoDebug
from apps.rooms.mutations import CreateRoom, WriteTurn
from apps.rooms.types import RoomType
from apps.rooms.models import Room, Turn
from apps.organizations.models import Organization
from graphene_subscriptions.events import CREATED, UPDATED, DELETED


class Query(graphene.ObjectType):
    debug_rooms = graphene.Field(
        DjangoDebug, name='__debug_rooms')
    room_by_code = graphene.Field(
        RoomType, code=graphene.String(), description='Информация о комнате по коду комнаты')
    rooms_in_organization = graphene.List(
        RoomType, subdomain=graphene.String(), description='Список комнат в организации')
    can_do_step_now_by_code = graphene.Boolean(code=graphene.String())

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


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    write_turn = WriteTurn.Field()


class Subscription(graphene.ObjectType):
    room_updated = graphene.Field(RoomType, code=graphene.String())

    def resolve_room_updated(root, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                user = info.context.user
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)
                print(room)
                return root.filter(
                    lambda event:
                    event.operation == UPDATED and
                    isinstance(event.instance, Room) and
                    event.instance.pk == int(room.id)
                ).map(lambda event: event.instance)
            else:
                raise Exception('Error code')
        except Exception as e:
            return None
