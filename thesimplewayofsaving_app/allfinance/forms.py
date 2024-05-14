from django import forms
from .models import Budget
from django.contrib.auth.forms import AuthenticationForm

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'value', 'date']
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})