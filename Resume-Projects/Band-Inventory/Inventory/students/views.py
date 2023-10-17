from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def sort_by_id(student):
    return student.id

def sort_by_first_name(student):
    return student.firstname.lower()

def sort_by_last_name(student):
    return student.lastname.lower()

def sort_by_address(student):
    return student.address.lower()

def sort_by_city(student):
    return student.city.lower()

def sort_by_state(student):
    return student.state.lower()

def sort_by_zip(student):
    return int(student.zip)

def sort_by_phone(student):
    return int(student.phone)

def sort_by_notes(student):
    return student.notes.lower()

def student_index(request):
    sort_by = request.GET.get('sort_by', 'id')
    reverse_sort = request.GET.get('reverse', 'false') == 'true'

    students = Student.objects.all()

    sorting_functions = {
        'id': sort_by_id,
        'firstname': sort_by_first_name,
        'lastname': sort_by_last_name,
        'address': sort_by_address,
        'city': sort_by_city,
        'state': sort_by_state,
        'zip': sort_by_zip,
        'phone': sort_by_phone,
        'notes': sort_by_notes,
    }

    sorting_function = sorting_functions.get(sort_by, sort_by_id)

    students = sorted(students, key=sorting_function, reverse=reverse_sort)

    context = {
        "students": students
    }

    return render(request, "students/index.html", context)

# Add a student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_index')  # Redirect to the student list page after adding.
    else:
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'students/add_student.html', context)

# View student details
def view_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/view_student.html', {'student': student})

# Edit student details
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:student_index')  # Redirect to the student list page after editing.
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'students/edit_student.html', context)