import graphene
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):
    debug_organizations = graphene.Field(
        DjangoDebug, name='__debug_organizations')


class Mutation(graphene.ObjectType):
    pass
