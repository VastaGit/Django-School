from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class PhoneBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(phone_number=phone_number)
            return user
        except User.DoesNotExist:
            pass
        return None
