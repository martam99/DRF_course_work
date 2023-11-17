import os
import requests
from celery import shared_task
from habit.models import Habit


def get_reward_or_habit():
    habits = Habit.objects.all()
    for habit in habits:
        reward = habit.reward
        pleasant = habit.pleasant_habit
        if reward:
            habit = reward
        else:
            habit = pleasant
        return habit


# @shared_task
# def habit_bot():
#     habits = Habit.objects.all()
#     for h in habits:
#         action = h.habit_action
#         time = h.time
#         place = h.place
#     text = f'Я должна {action} в {time} в {place}' \
#            f'После этого {get_reward_or_habit()}'
#     params = {"chat_id": os.getenv('CHANNEL_ID'), 'text': text}
#     requests.get(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage", params=params)


# bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
# bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)


@shared_task
def habit_bot():
    send_habit = Habit.objects.all()
    for h in send_habit:
        action = h.habit_action
        time = h.time
        place = h.place
        text = f'Я должна {action} в {time} в {place}'
        params = {"chat_id": os.getenv('CHANNEL_ID'), 'text': text}
        requests.get(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage", params=params)
