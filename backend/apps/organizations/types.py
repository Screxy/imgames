from .models import Organization
from graphene_django.types import DjangoObjectType


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"
