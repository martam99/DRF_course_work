from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habit.models import Habit
from user.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            is_active=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.user.set_password('qwe123rty456')
        self.user.save()

        self.habit = Habit.objects.create(
            place='Home',
            habit_action='Drink water',
            reward='eat apple',
            time_to_complete=80
        )
        self.habit.save()

    def test_create_habit(self):
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': self.habit.reward,
            'time_to_complete': self.habit.time_to_complete
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
            1
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

    def tearDown(self):
        User.objects.all().delete()
        Habit.objects.all().delete()
