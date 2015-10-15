from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import UserLoginForm
# Create your views here.

class LogInView(FormView):

	template_name = 'users/login.html'
	form_class = UserLoginForm


class UserRegisterView(TemplateView):

	template_name = 'users/register.html'