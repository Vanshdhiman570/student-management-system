from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import StudentForm
from django.contrib import messages
from .models import Student

# Create your views here.
@login_required
def home(request):
   students = Student.objects.all()
   total_student = students.count()
   return render(request, 'home.html', {"total_student": total_student})

@login_required
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


@login_required
def view_students(request):
    search_query = request.GET.get('search')

    if search_query:
        students = Student.objects.filter(name__icontains=search_query)

    else:
        students = Student.objects.all()
        
    paginator = Paginator(students, 5) # Five students per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_student.html', {"page_obj": page_obj})


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('view_students')

@login_required
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
