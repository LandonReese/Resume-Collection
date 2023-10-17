from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path("students/", views.student_index, name='student_index'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:student_id>/', views.view_student, name='view_student'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
]