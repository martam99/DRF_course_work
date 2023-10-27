from django.contrib import admin

from habit.models import Habit


# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('owner', 'place', 'time', 'habit_action',
                    'pleasant_habit', 'is_pleasant', 'period',
                    'reward', 'time_to_complete', 'is_public')
