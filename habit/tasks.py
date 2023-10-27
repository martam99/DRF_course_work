import os

from celery import shared_task
import telegram

from habit.models import Habit


@shared_task
def habit_bot():
    queryset = Habit.objects.all()
    text = f'я буду {queryset.habit_action} в {queryset.time} в {queryset.place}'
    bot = telegram.Bot(token=os.getenv('bot_token'))
    bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)
    habit_bot.delay()
