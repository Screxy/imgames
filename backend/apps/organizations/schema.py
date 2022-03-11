import graphene
from graphene_django.debug import DjangoDebug
from organizations.mutations import CreateOrganization
from organizations.types import OrganizationType
from organizations.models import Organization


class Query(graphene.ObjectType):
    debug_organizations = graphene.Field(
        DjangoDebug, name='__debug_organizations')
    organizations_by_user = graphene.List(OrganizationType)

    def resolve_organizations_by_user(root, info, **kwargs):
        """Список организаций для конкретного пользователя"""
        user = info.context.user
        return Organization.objects.filter(organization_owner=user).order_by('id')


class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
