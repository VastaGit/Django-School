from django.urls import path, include
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('students/', views.students, name='students'),
    path('', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls'), {'extra_context': {'next_page': reverse_lazy('admin:index')}}),
    path('send_email/', views.send_email_form, name='send_email'),
]
