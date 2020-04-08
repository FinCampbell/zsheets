from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from timesheet.models import Employee

# Create your views here.

class BasicView(DetailView):
  model = Employee
  
class LoginView(TemplateView):
  template_name = "timesheet/login.html"
  
class RegisterView(TemplateView):
  template_name = "timesheet/register.html"