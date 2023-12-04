from django import forms
from .models import *

class adminform(forms.ModelForm):
    class Meta:
        model=admins
        fields='__all__'

class updateadminform(forms.ModelForm):
    class Meta:
        model=admins
        fields=['firstname', 'lastname', 'username', 'password']

class managerform(forms.ModelForm):
    class Meta:
        model=manager
        fields='__all__'

class updatemanagerform(forms.ModelForm):
    class Meta:
        model=manager
        fields=['firstname', 'lastname', 'username', 'password', 'pharmacy_name']

class medicineform(forms.ModelForm):
    class Meta:
        model=medicine
        fields='__all__'

class updatemedicine(forms.ModelForm):
    class Meta:
        model=medicine
        fields=['name', 'category', 'Qty', 'price']