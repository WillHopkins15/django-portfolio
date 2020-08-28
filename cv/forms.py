from django import forms
from .models import Cv

class CvForm(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('name','curr_employment','address','phone','email','links','skills','hobbies','profile','employment_hist','education','references',)