from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    status_choices = [('active', 'Active'), ('blocked', 'Blocked')]
    name = forms.CharField(max_length=50, required=True, label='Name')
    email = forms.EmailField(max_length=50, required=True, label='Email')
    text = forms.CharField(max_length=100, required=True, label='Text',
                           widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
