import graphene
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):
    debug_flows = graphene.Field(DjangoDebug, name='__debug_flows')


class Mutation(graphene.ObjectType):
    pass
