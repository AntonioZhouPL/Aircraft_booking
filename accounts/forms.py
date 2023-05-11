from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Admin, Engineer, Employee


class UserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user
