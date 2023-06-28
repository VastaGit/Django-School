from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    subject_name = forms.CharField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'subject_name']

from django import forms
