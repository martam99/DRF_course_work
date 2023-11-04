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

        self.pleasant_habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            is_pleasant=True
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_action='Drink water',
            pleasant_habit=self.pleasant_habit
        )

    def tearDown(self):
        User.objects.all().delete()
        Habit.objects.all().delete()

    def test_create_habit(self):
        """Тест для создания привычки"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': "eat apple",
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 3)

    def test_create_habit_err1(self):
        """Тест для проверки валидатора"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "You haven't filled in one of these fields. Please, fill in one of the two ("
                                 "nice_habit/reward) fields"
                             ]
                         }
                         )

    def test_create_habit_err2(self):
        """Тест для проверки валидатора"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': 'Eat sweet',
            'pleasant_habit': self.pleasant_habit.id
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Please, fill in one of the two (nice_habit/reward) fields"
                             ]
                         }
                         )

    def test_create_habit_err3(self):
        """Тест для проверки валидатора"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': 'Eat sweet',
            'time_to_complete': "00:25:00"
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Please, write correct time. Time must be less than 120 seconds"
                             ]
                         }
                         )
