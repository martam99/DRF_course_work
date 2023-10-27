import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule

from habit.models import Habit

if Habit.objects.period == 'DAILY':
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS,
    )
elif Habit.objects.period == 'WEEKLY':
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=7,
        period=IntervalSchedule.DAYS,
    )

PeriodicTask.objects.create(
    interval=schedule,
    name='Habit reminder',
    task='habit.tasks.habit_bot',
    args=json.dumps(['arg1', 'arg2']),
    kwargs=json.dumps({
        'be_careful': True,
    }),
    start_time=Habit.objects.time,
    expires=datetime.utcnow() + timedelta(seconds=30)
)
