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





#
# Projects

# Student Management System | Django

# Built a web-based student management application with CRUD functionality.

# Implemented forms for adding and editing student data.

# Displayed student records in a table with edit and delete actions.

# Used Django messaging framework for success notifications.

# Contact Book Application | Django

# Developed a contact management web application using Django.

# Implemented CRUD operations with search functionality.

# Added JavaScript confirmation popup before deleting contacts.

# Displayed contacts in a table with edit and delete options.#