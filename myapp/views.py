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

            form.save()
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
