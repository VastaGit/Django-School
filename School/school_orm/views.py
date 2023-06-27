from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm


def students(request):
  myStudents = Student.objects.all().values()
  template = loader.get_template('all_students.html')
  context = {
    'myStudents': myStudents,
  }
  return HttpResponse(template.render(context, request))

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})