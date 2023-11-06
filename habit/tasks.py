import os

import requests
from celery import shared_task
import telegram
from habit.models import Habit

habits = Habit.objects.all()
for h in habits:
    action = h.habit_action
    time = h.time
    place = h.place
    reward = h.reward
    pleasant = h.pleasant_habit


def get_reward_or_habit():
    if reward:
        habit = reward
    else:
        habit = pleasant
    return habit


@shared_task
def habit_bot():
    text = f'Я должна {action} в {time} в {place}' \
           f'После этого {get_reward_or_habit()}'
    params = {"chat_id": os.getenv('CHANNEL_ID'), 'text': text}
    requests.get(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage", params=params)
    # bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
    # bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)


habit_bot.delay()
