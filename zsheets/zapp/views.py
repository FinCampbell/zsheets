from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Employee

def login(request):
    return redirect('/accounts/login/')

@login_required
def user_dashboard(request):
    return render(request, 'zapp/dashboard.html', {})

def submit_timesheet(request):
    return HttpResponse("This is where you submit timesheets")

def view_schedule(request):
    return HttpResponse("This is where you view your schedule, approved timesheets")

#upper management pages

def search_schedules(request):
    return HttpResponse("This is where you search for schedules")

def approve_timesheets(request):
    return HttpResponse("This is where you approve timesheets")
