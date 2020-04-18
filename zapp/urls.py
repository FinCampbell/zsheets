from django.urls import path, include

from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    
   # path('accounts/', include('django.contrib.auth.urls')),

    path('', views.login, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('submit_timesheet/', views.submit_timesheet, name='submit_timesheet'),
    path('my_schedule/', views.my_schedule, name='my_schedule'),
    path('search_schedules/', login_required(views.EmployeeSearchView.as_view()), name='search_schedules'),
    path('approve_timesheets/', views.approve_timesheets, name='approve_timesheets')
]

