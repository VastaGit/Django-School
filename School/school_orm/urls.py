from django.urls import path, include
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('students/', views.students, name='students'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls'), {'extra_context': {'next_page': reverse_lazy('admin:index')}}),
]