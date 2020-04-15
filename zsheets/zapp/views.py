from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import TimesheetForm
from .models import Employee

def login(request):
    return redirect('/accounts/login/')

@login_required
def user_dashboard(request):
    return render(request, 'zapp/dashboard.html', {})

def submit_timesheet(request):
    if request.method == "POST":
        form = TimesheetForm(request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.employee = request.user.employee
            timeseet.save()
            return HttpResponse("Your submission has been successful, please wait for your managers approval.")
    else:
        form = TimesheetForm()
    return render(request, 'zapp/submit_timesheet.html', {'form' : form})

def view_schedule(request):
    return HttpResponse("This is where you view your schedule, approved timesheets")

#upper management pages

def search_schedules(request):
    return HttpResponse("This is where you search for schedules")

def approve_timesheets(request):
    return HttpResponse("This is where you approve timesheets")
