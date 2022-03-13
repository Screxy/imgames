import graphene
from graphene_django.debug import DjangoDebug
from .mutations import CreateRoom
from .types import RoomType
from .models import Room
from organizations.models import Organization


class Query(graphene.ObjectType):
    debug_rooms = graphene.Field(
        DjangoDebug, name='__debug_rooms')
    rooms_in_organization = graphene.List(
        RoomType, subdomain=graphene.String(), description='Список комнат в организации')

    def resolve_rooms_in_organization(root, info, subdomain):
        try:
            organization = Organization.objects.get(subdomain=subdomain)
            return Room.objects.filter(organization=organization)
        except Exception as e:
            return None


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
