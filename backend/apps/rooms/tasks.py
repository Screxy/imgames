from hashlib import new
from celery import shared_task
from apps.organizations.models import Organization
from apps.rooms.models import Room, Month, Turn
from apps.flows.models import Stage, Channel
from apps.computed.models import ChannelComputed, StageComputed
from graphene_subscriptions.events import SubscriptionEvent
from django.forms.models import model_to_dict
import json

MONTH_EVENT = 'month_event'


@shared_task
def adding_task(x, y):
    return x + y


@shared_task
def change_month_in_room(room_id):
    try:
        room = Room.objects.get(pk=room_id)
        current_round = room.current_round
        old_month = current_round.current_month

        # 1. Записываем в computed начальные значения

        # Получаем набор шагов за прошедший игровой месяц
        old_month_users_turns = Turn.objects.filter(month=old_month)
        print(old_month_users_turns)

        # Если месяц был в комнате начальным (шаг игрока №1)
        if old_month.key == 0:

            # TODO: Получаем каналы по умолчанию
            channels = Channel.objects.filter(flow=room.flow)

            # TODO: Получаем этапы по умолчанию
            stages = Stage.objects.filter(flow=room.flow)

            # Для каждого шага-пользователя за месяц
            for turn in old_month_users_turns:
                # Для каждого этапа записываем вычисляемое значение c конверсией по умолчанию
                for stage in stages:
                    StageComputed.objects.create(
                        turn=turn, stage=stage, conversion=stage.conversion)

                # Для каждого канала записываем связку Ход + Этап
                for channel in channels:
                    ChannelComputed.objects.create(
                        turn=turn, channel=channel, cardinal_value=channel.default_value)

        # Если месяц был не начальным
        else:
            prev_old_month = Month.objects.get(
                key=(old_month.key-1), round=current_round)
            prev_old_month_users_turns = Turn.objects.filter(
                month=prev_old_month)

            for prev_turn in prev_old_month_users_turns:
                # Получаем новый шаг
                turn = Turn.objects.get(user=prev_turn.user, month=old_month)

                # Получаем этапы предыдущего шага
                prev_computed_stages = StageComputed.objects.filter(
                    turn=prev_turn)

                # Для каждого этапа предыдущего шага
                for old_computed_stage in prev_computed_stages:
                    # Дублируем запись в вычисляемых значениях со ссылкой на новый ход
                    StageComputed.objects.create(
                        turn=turn, stage=old_computed_stage.stage, conversion=old_computed_stage.conversion)

                # Получаем каналы предыдущего шага
                prev_computed_channels = ChannelComputed.objects.filter(
                    turn=prev_turn)

                # Для каждого канала предыдущего шага
                for old_computed_channel in prev_computed_channels:
                    # Дублируем запись в вычисляемых значениях со ссылкой на новый ход
                    ChannelComputed.objects.create(
                        turn=turn, channel=old_computed_channel.channel, cardinal_value=old_computed_channel.cardinal_value)

            # 2. Для каждого изменения из-за карточек обновляем данные
            # TODO: для каждого шага получаем набор выборов карточек
            # TODO: для каждого выбора карточек получаем карточку
            # TODO: для каждой карточки получаем набор изменения параметров
            # Для каждого изменения карточки
            # - если изменение начального параметра
            # - если изменение конверсии этапа

            # Высчитываем следующий номер месяца
        new_key = old_month.key+1

        # TODO: check that the new month is not bigger than the maximum key

        # Находим следующий номер месяца
        new_month = Month.objects.filter(key=new_key, round=current_round)

        # Если нет следующего месяца
        if len(new_month) < 1:
            print('ERROR')
            # TODO: send final
            raise Exception('Error month')
        current_round.current_month = new_month[0]
        current_round.save()

        # Отправляем всем событие на обновление состояния комнаты
        # TODO: проверить, что корректно обновляется раунд
        room.current_round = current_round
        month_event = SubscriptionEvent(
            operation=MONTH_EVENT,
            instance=model_to_dict(room))
        print("--> EVENT")
        month_event.send()

        # TODO: send update on
        return new_month[0].key
    except Exception as e:
        print('TASK ERROR -------------------------')
        print(e)
        print('TASK ERROR -------------------------')
        return None
