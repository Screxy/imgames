import graphene
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):
    debug_rooms = graphene.Field(DjangoDebug, name='__debug_rooms')


class Mutation(graphene.ObjectType):
    pass
