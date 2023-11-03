import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule
from habit.models import Habit
habit = Habit.objects.all()
for h in habit:
    periods = h.period
    time = h.time

    if periods == 'DAILY':
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )
    elif periods == 'WEEKLY':
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
        start_time=time,
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
