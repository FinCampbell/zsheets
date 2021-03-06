from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import TimesheetForm
from .models import Employee, Timesheet, User

def login(request):
    return redirect('/accounts/login/')

class success(TemplateView):
  template_name = 'zapp/success.html'
  
class approve_success(TemplateView):
  template_name = 'zapp/approve_success.html'
  
class error(TemplateView):
  template_name = 'zapp/error.html'
  
@login_required
def user_dashboard(request):
    return render(request, 'zapp/dashboard.html', {})

@login_required
def submit_timesheet(request):
    if request.method == "POST":
        form = TimesheetForm(request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.employee = request.user.employee
            timesheet.username = request.user.username
            timesheet.save()
            return redirect("zapp:success")
    else:
        form = TimesheetForm()
    return render(request, 'zapp/submit_timesheet.html', {'form' : form})

@login_required
def my_schedule(request):
    my_timesheets = Timesheet.objects.filter(employee = request.user.employee, approved_status=True)
    context = {'my_timesheets' : my_timesheets}
    return render(request, 'zapp/my_schedule.html',context)

#upper management pages

#@permission_required('zapp.can_search')
class EmployeeSearchView(PermissionRequiredMixin, ListView):
  permission_required = ('zapp.can_approve')
  model = Timesheet
  template_name = 'zapp/search_timesheet.html'
  
  def get_queryset(self):
    query = self.request.GET.get('q')
    if Timesheet.objects.filter(username__iexact=query).exists():
      object_list =  Timesheet.objects.filter(username__iexact=query)
    else:
      object_list = None
    return object_list

  
@permission_required('zapp.can_approve')
def approve_timesheets(request):
    if request.method == "POST":
        try:
            timesheet = Timesheet.objects.get(id=request.POST['timesheet'])
            
        except (KeyError, Timesheet.DoesNotExist):
            return redirect("zapp:error")

        else:
            timesheet.approved_status = True
            timesheet.save()
            return redirect("zapp:approve_success")
    else:
        pending_timesheets = Timesheet.objects.filter(approved_status=False)
    return render(request, 'zapp/approve_timesheets.html', {'pending_timesheets' : pending_timesheets})
  
