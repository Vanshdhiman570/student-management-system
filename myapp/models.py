from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
    name = models.CharField(max_length=50)

    roll_no = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                r'^\d{10}$',
                'Roll number must be exactly 10 digits'
            )
        ]
    )

    email = models.EmailField()
    course = models.CharField(max_length=100)
