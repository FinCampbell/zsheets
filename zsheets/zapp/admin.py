from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Employee, Manager, Timesheet

class TimesheetInline(admin.StackedInline):
    model = Timesheet

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [TimesheetInline]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manager)

