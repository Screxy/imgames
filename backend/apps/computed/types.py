import graphene
from apps.flows.types import ChannelType


class ComputedGameDataType(graphene.ObjectType):
    data = graphene.List(graphene.Int, array=graphene.List(graphene.Int))
    channel = graphene.Field(ChannelType)
