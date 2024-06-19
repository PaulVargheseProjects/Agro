from django import forms
from .models import LabResult

class LabResultForm(forms.ModelForm):
    """Form definition for LabResult."""

    class Meta:
        """Meta definition for LabResultform."""

        model = LabResult
        exclude = ('lab_appointment',)


