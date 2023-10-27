from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from user.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            is_active=True
        )
        self.user.set_password('qwe123rty456')
        self.user.force_authenticated(user=self.user)
        self.user.save()

        self.habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_action='Drink water',
            period='DAILY',
            reward='eat apple',
        )
        self.habit.save()

    def test_create_habit(self):
        data = {
            "owner": self.user,
            "place": 'Test',
            "habit_action": 'Test2',
            "period": 'DAILY',
            "reward": 'Test3',
        }
        response = self.client.post(
            reverse('habit:create-habit'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

    def test_list_lesson(self):
        """test for list of lessons"""
        response = self.client.get(
            reverse('habit:list-habit'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

