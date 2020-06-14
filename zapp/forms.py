from django import forms

from .models import Timesheet

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class TimesheetForm(forms.ModelForm):
  
  def no_neg(value):
    if value < 0:
      raise ValidationError(
        _('%(value)s is negative'),
        params={'value': value},
      )
   
  
  week_beginning = forms.DateField()
  monday = forms.IntegerField(validators=[no_neg])
  tuesday = forms.IntegerField(validators=[no_neg])
  wednesday = forms.IntegerField(validators=[no_neg])
  thursday = forms.IntegerField(validators=[no_neg])
  friday = forms.IntegerField(validators=[no_neg])
   
  class Meta:
    model = Timesheet
    fields = ('week_beginning', 'monday', 'tuesday' , 'wednesday' ,'thursday', 'friday',)
