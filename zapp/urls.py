from django.urls import path, include

from django.contrib.auth.decorators import login_required

from . import views

app_name = "zapp"
urlpatterns = [
    
   # path('accounts/', include('django.contrib.auth.urls')),

    path('', views.login, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('submit_timesheet/', views.submit_timesheet, name='submit_timesheet'),
    path('my_schedule/', views.my_schedule, name='my_schedule'),
    path('search_schedules/', login_required(views.EmployeeSearchView.as_view()), name='search_schedules'),
    path('approve_timesheets/', views.approve_timesheets, name='approve_timesheets'),
    path('success/', views.success.as_view(), name="success"),
    path('approve_success/', views.approve_success.as_view(), name="approve_success"),
    path('error/', views.error.as_view(), name="error"),
]

