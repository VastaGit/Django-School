from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm
from django.contrib.auth import get_user_model

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            create_superuser(user)
            return redirect('/accounts/login/')
    return render(req, 'register.html', {'form': form})


# SendUserEmails view class
def send_email_form(request):
    if request.method == 'POST':
        # Retrieve the form data
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user_ids = request.GET.get('user_ids').split('-')

        # Get the selected users
        students = Student.objects.filter(id__in=user_ids)

        # Send the email to selected users
        for student in students:
            send_mail(subject, message, 'askatseitakunov@gmail.com', [student.mail])

        # Redirect to a success page or the admin page
        return HttpResponseRedirect('/admin/') 

    return render(request, 'email_form.html')

def create_superuser(user):
    User = get_user_model()
    superuser = User.objects.get(pk=user.pk)
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()