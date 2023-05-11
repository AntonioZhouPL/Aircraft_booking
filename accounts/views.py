from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserSignUpForm

class UserSignUpView(generic.CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


