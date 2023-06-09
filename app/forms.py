from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import Login, Preferences, Application


class DateInput(forms.DateInput):
    input_type = 'date'

class JobseekerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('name', 'phone', 'email','address', 'location','Required_job','Qualification','Experience', 'username', 'password1', 'password2')

class RecuiterForm(UserCreationForm):
    class Meta:
        model = Login
        fields = (
        'name', 'phone', 'email', 'address', 'companyname', 'jobTitle', 'companyname','registrationNo', 'username',
        'password1', 'password2')
class PreferencesForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Preferences
        fields = ('Companyname','location','jobTitle','Qualification','Experience','salary','Description','date')
class ApplicationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Application
        fields = ("resume", "applicant",'job','company' ,'date')
#
# class ApplicationForm(forms.ModelForm):
#     date = forms.DateField(widget=DateInput)
#     class Meta:
#         model = Application
#         fields = ('company','job','applicant','resume','date')







