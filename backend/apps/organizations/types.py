from .models import Organization, OrganizationSettings
from graphene_django.types import DjangoObjectType


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationSettingsType(DjangoObjectType):
    class Meta:
        model = OrganizationSettings
        fields = "__all__"
