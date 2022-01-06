import graphene
from graphene_django.debug import DjangoDebug
from .mutations import CreateRoom


class Query(graphene.ObjectType):
    debug_rooms = graphene.Field(DjangoDebug, name='__debug_rooms')


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
