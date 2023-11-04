import os

import requests
import telebot
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
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHANNEL_ID')
    text = f'я буду {action} в {time} в {place}' \
           f'После этого {get_reward_or_habit()}'
    params = {'chat_id': chat_id, 'text': text}
    requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage', params=params)
    # bot = telebot.TeleBot(token=os.getenv('BOT_TOKEN'))
    # text = f'я буду {action} в {time} в {place}' \
    #        f'После этого {get_reward_or_habit()}'
    # bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)
    # @bot.message_handler(commands=["start"])
    # def start(m, res=False):
    #     text = f'я буду {action} в {time} в {place}' \
    #            f'После этого {get_reward_or_habit()}'
    #     bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)

    # text = f'я буду {action} в {time} в {place}' \
    #        f'После этого {get_reward_or_habit()}'
    # bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
    # bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)


habit_bot.delay()
