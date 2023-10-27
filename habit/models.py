import datetime

from django.db import models

from user.models import User, NULLABLE


# Create your models here.
# Пользователь — создатель привычки.+
# Место — место, в котором необходимо выполнять привычку. +
# Время — время, когда необходимо выполнять привычку. +
# Действие — действие, которое представляет собой привычка. +
# Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки. +
# Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных. +
# Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях. +
# Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
# Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
# Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.


class Habit(models.Model):
    PERIOD = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время', **NULLABLE)
    habit_action = models.TextField(verbose_name='действие')
    pleasant_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Приятная привычка', **NULLABLE)
    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки', default=False)
    period = models.CharField(max_length=15, verbose_name='Периодичность', choices=PERIOD, default='DAILY')
    reward = models.TextField(verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='Время на выполнение в секундах', default=datetime.time(minute=2))
    is_public = models.BooleanField(verbose_name='Признак публичности', default=False)

    objects = models.Manager()

    def __str__(self):
        return f"{self.habit_action}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
