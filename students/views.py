from django.shortcuts import render
from django.views.generic import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'students/students_list.html'
    context_object_name = 'students'
    paginate_by = 1