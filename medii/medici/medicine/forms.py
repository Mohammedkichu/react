from django import forms
from medicine.models import Medicine
from django.forms import ModelForm

class Medicineforms(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = "__all__"
        