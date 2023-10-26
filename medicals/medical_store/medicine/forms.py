from django import forms
from medicine.models import Medicine

class Medicineforms(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = "__all__"
        