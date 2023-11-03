import datetime

from rest_framework.exceptions import ValidationError


class HabitValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, val):
        field1 = dict(val).get(self.field1)
        field2 = dict(val).get(self.field2)
        field3 = dict(val).get(self.field3)
        if field1 is None and field2 is None:
            raise ValidationError(
                "You haven't filled in one of these fields. Please, fill in one of the two (nice_habit/reward) fields")
        elif field1 and field2:
            raise ValidationError('Please, fill in one of the two (nice_habit/reward) fields')
        elif field1 is None and field3 is False:
            raise ValidationError("Your pleasant habit hasn't positive sign")


class HabitTimeValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, field):
        val = dict(field).get(self.fields)
        if val and val > datetime.time(minute=2):
            raise ValidationError('Please, write correct time. Time must be less than 120 seconds')

