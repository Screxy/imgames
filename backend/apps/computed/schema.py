import graphene
from graphene_django.debug import DjangoDebug
from .types import ComputedGameDataType
from organizations.models import Organization
from apps.rooms.models import Room
from apps.flows.models import Channel


class Query(graphene.ObjectType):
    debug_computed = graphene.Field(DjangoDebug, name='__debug_computed')
    computed_channels_by_code = graphene.List(ComputedGameDataType, code=graphene.String(
    ), description='Игровые данные пользователя на текущий месяц по коду комнаты')

    def resolve_computed_channels_by_code(root, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)

                # TODO:
                # - Какой месяц в комнате текущий?
                # - Находим по текущему месяцу текущий шаг
                # -
                return [ComputedGameDataType(data=[5, 6], channel=Channel.objects.first()), ComputedGameDataType(data=[5, 6], channel=Channel.objects.first()), ]
            else:
                raise Exception('Error code')
        except Exception as e:
            return None


class Mutation(graphene.ObjectType):
    pass
