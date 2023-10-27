import os

from celery import shared_task
import telegram

from habit.models import Habit


@shared_task
def habit_bot():
    habit = Habit.objects.all()
    text = f'я буду  в {Habit.objects.time}'
    bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
    bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)
    habit_bot.delay()
# {habit.habit_action} {habit.time} в {habit.place}