from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitValidator, HabitTimeValidator, IsPleasant


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(field1='pleasant_habit', field2='reward'),
                      HabitTimeValidator(fields='time_to_complete'),
                      IsPleasant(fields='is_pleasant')]
                      #IntervalForHabit(fields='period')]

