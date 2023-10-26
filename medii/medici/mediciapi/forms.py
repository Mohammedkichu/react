from django import forms


class Medicineform(forms.Form):
    username = forms.CharField(required=True, error_messages={'errors': 'Username already exists'})
    emailid = forms.CharField(required=True)
    password = forms.CharField(required=True,)
