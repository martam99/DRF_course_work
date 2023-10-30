import os
from celery import shared_task
import telegram
from habit.models import Habit


@shared_task
def habit_bot():
    habit = Habit.objects.habit_action
    time = Habit.objects.time
    place = Habit.objects.place
    text = f'я буду {habit} в {time} в {place}'
    bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
    bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)
    habit_bot.delay()
