import os
from celery import shared_task, Celery
import telegram
from habit.models import Habit

habits = Habit.objects.all()


def get_reward_or_habit():
    for h in habits:
        reward = h.reward
        pleasant = h.pleasant_habit
        if reward:
            habit = reward
        else:
            habit = pleasant
        return habit


@shared_task
def habit_bot():
    for habit in habits:
        action = habit.habit_action
        time = habit.time
        place = habit.place
        text = f'я буду {action} в {time} в {place}' \
               f'После этого {get_reward_or_habit()}'
        bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
        bot.send_message(chat_id=os.getenv('CHANNEL_ID'), text=text)
        result = habit_bot.delay()
        return result
