from hashlib import new
from celery import shared_task
from apps.organizations.models import Organization
from apps.rooms.models import Room, Month
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
        print(e)
        return None
