from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Student, Teaches, Studies

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'subject_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'subject_name'),
        }),
    )
    list_display = ('phone_number', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('phone_number',)


@admin.action(description="Send email to selected")
def send_group_email(modeladmin, request, queryset):
    
    selected_user_ids = queryset.values_list('id', flat=True)
    # Redirect to the custom email form
    url = reverse('send_email')  # Replace 'send_email_form' with the URL name of your email form view
    url += f'?user_ids={"-".join(str(user_id) for user_id in selected_user_ids)}'
    return HttpResponseRedirect(url)



class StudentAdmin(admin.ModelAdmin):
    search_fields=('name',)
    list_display = ["name", "mail"]
    ordering = ["name"]
    actions = [send_group_email]


admin.site.register(get_user_model(), CustomUserAdmin)

admin.site.register(Student, StudentAdmin)

admin.site.register(Studies)

admin.site.register(Teaches)