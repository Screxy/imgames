from decimal import Decimal
import graphene
from graphene_django.debug import DjangoDebug
from .types import ComputedGameDataType
from apps.organizations.models import Organization
from apps.rooms.models import Room
from apps.flows.models import Channel, Stage


class Query(graphene.ObjectType):
    debug_computed = graphene.Field(DjangoDebug, name='__debug_computed')
    computed_channels_by_code = graphene.List(ComputedGameDataType, code=graphene.String(
    ), description='Игровые данные пользователя на текущий месяц по коду комнаты')

    def resolve_computed_channels_by_code(root, info, code):
        try:
            code_array = str(code).split('-')
            if len(code_array) > 1:
                user = info.context.user
                organization = Organization.objects.get(
                    prefix__iexact=code_array[0])
                room = Room.objects.get(
                    key=code_array[1], organization=organization)

                # Находим текущий месяц
                current_month = room.current_round.current_month

                # Находим текущий механику комнаты
                flow = room.flow

                # Находим данные о каналах по умолчанию
                channels = Channel.objects.filter(flow=flow)

                # Находим данные о этапах воронки по умолчанию
                stages = Stage.objects.filter(flow=flow)

                answer_array = []
                # if current_month.key == 0:
                total_data = [Decimal(0)]
                for i in range(len(stages)):
                    total_data += [Decimal(0), Decimal(0)]

                for channel in channels:

                    # Находим входное значение канала
                    channel_start_value = channel.default_value
                    data = [channel_start_value]
                    total_data[0] += channel_start_value
                    # Вычисляем значение для каждого этапа воронки
                    channel_next = channel_start_value
                    for i, stage in enumerate(stages, start=0):

                        # Высчитываем значение после конверсии
                        channel_next = channel_next * stage.conversion

                        #
                        total_data[1+(2*i)
                                   ] = '{0:.2f}'.format(Decimal(total_data[1+(2*i)])+Decimal(0))
                        total_data[2+(2*i)] = '{0:.2f}'.format(
                            Decimal(channel_next)+Decimal(total_data[2+(2*i)]))

                        # Форматируем данные для ответа
                        data += ['{0:.2f}'.format(stage.conversion),
                                 '{0:.2f}'.format(channel_next)]

                    # Добавляем данные в массив возвращаемых значений
                    answer_array += [ComputedGameDataType(
                        data=data, channel=channel, is_total=False)]

                # Добавляем значение ИТОГО
                answer_array += [ComputedGameDataType(
                    data=total_data, channel=None, is_total=True)]

                return answer_array
            else:
                raise Exception('Error code')
        except Exception as e:
            print(e)
            return None


class Mutation(graphene.ObjectType):
    pass
