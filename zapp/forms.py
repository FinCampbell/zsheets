from django import forms

from .models import Timesheet


class TimesheetForm(forms.ModelForm):

    class Meta:
        model = Timesheet
        fields = ('week_beginning', 'monday', 'tuesday' , 'wednesday' ,'thursday', 'friday',)

class EmployeeSearch(forms.Form):
  userID = forms.CharField(max_length=255)