from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

def students(request):
  myStudents = Student.objects.all().values()
  template = loader.get_template('all_students.html')
  context = {
    'myStudents': myStudents,
  }
  return HttpResponse(template.render(context, request))