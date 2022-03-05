import graphene
from graphene_django.debug import DjangoDebug
from organizations.mutations import CreateOrganization


class Query(graphene.ObjectType):
    debug_organizations = graphene.Field(
        DjangoDebug, name='__debug_organizations')


class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
