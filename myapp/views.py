from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib import messages
from .models import Student

# Create your views here.
def home(request):
   students = Student.objects.all()
   total_student = students.count()
   return render(request, 'home.html', {"total_student": total_student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            # name = form.cleaned_data['name']
            # roll_no = form.cleaned_data['roll_no']
            # email = form.cleaned_data['email']
            # course = form.cleaned_data['course']

            form.save()
            # Student.objects.create(name=name, roll_no=roll_no, email=email, course=course)
            messages.success(request, "Student added successfully!")
            
            return redirect('add_student')
    else:        
        form = StudentForm()

    return render(request, 'add_student.html', {"form": form})


def view_students(request):
    search_query = request.GET.get('search')

    if search_query:
        students = Student.objects.filter(name__icontains=search_query)

    else:
        students = Student.objects.all()

    return render(request, 'view_student.html', {"students": students})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('view_students')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {"form": form})




# =========================================================

# Update it to something like this:

# Technical Skills

# Programming: Python

# Framework: Django

# Web Technologies: HTML, CSS

# Concepts: CRUD Operations, Form Handling, Exception Handling

# Tools: Git (Basic), VS Code

# You were unsure about adding HTML & CSS, but you should include them because:

# Django templates use HTML

# Styling uses CSS

# Recruiters expect them in a Django profile

# You don’t need to claim advanced CSS, just listing them is fine.

# 2️⃣ Update Your Projects Section

# Your resume currently shows Python CLI projects, but now you have Django web projects, which are stronger.

# Replace your projects with these:

# Student Management System | Django

# Developed a web-based system to manage student records using Django.

# Implemented CRUD operations to add, view, update, and delete student data.

# Displayed student records in a table with edit and delete actions.

# Added search functionality and success messages for user feedback.

# Contact Book Application | Django

# Built a web application to manage personal contacts using Django.

# Implemented CRUD functionality for adding, editing, and deleting contacts.

# Added search feature to find contacts by name.

# Implemented JavaScript confirmation popup before deleting contacts.

# 3️⃣ One Small Resume Improvement (Important)

# Your Objective currently says:

# "Motivated BCA student seeking a Python Internship..."

# Since you now work with Django, change it to:

# Objective

# Motivated BCA student seeking a Python/Django internship to apply programming and web development skills in building real-world applications.

# This aligns better with your new skills.