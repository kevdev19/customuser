from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUserModel
    # field_display_list = ['username', 'displayname']

    """
    Code adapted from the following link:
    https://tinyurl.com/y3obxwdt
    """
    fieldsets = (
        *UserAdmin.fieldsets,
            'Additional User Fields',
            {
                'fields': (
                    'age',
                    'displayname',
                    'homepage',
                ),
            },
        ),
    )


admin.site.register(CustomUserModel, CustomUserAdmin)
