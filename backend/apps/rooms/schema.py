import graphene
from graphene_django.debug import DjangoDebug
from .mutations import CreateRoom
from .types import RoomType
from .models import Room
from organizations.models import Organization


class Query(graphene.ObjectType):
    debug_rooms = graphene.Field(
        DjangoDebug, name='__debug_rooms')
    room_by_code = graphene.Field(
        RoomType, code=graphene.String(), description='Информация о комнате по коду комнаты')
    rooms_in_organization = graphene.List(
        RoomType, subdomain=graphene.String(), description='Список комнат в организации')

    def resolve_rooms_in_organization(root, info, subdomain):
        try:
            organization = Organization.objects.get(subdomain=subdomain)
            return Room.objects.filter(organization=organization)
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
