from django import forms
from .models import Land, Product, LabAppointment, UserQuery

class LandForm(forms.ModelForm):
    """Form definition for Land."""

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    class Meta:
        """Meta definition for Landform."""

        model = Land
        exclude = ('user',)

class ProductForm(forms.ModelForm):
    """Form definition for Product."""

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    class Meta:
        """Meta definition for Productform."""

        model = Product
        exclude = ('user',)


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class LabAppointmentForm(forms.ModelForm):
    """Form definition for LabAppointment."""
    
    date = forms.DateField(widget=DateInput())
    time = forms.TimeField(widget=TimeInput(
        attrs={'min':'07:00', 'max':'17:00'}
    ))

    class Meta:
        """Meta definition for LabAppointmentform."""

        model = LabAppointment
        exclude = ('user', 'status', 'test')

class UserQueryForm(forms.ModelForm):
    """Form definition for UserQuery."""

    class Meta:
        """Meta definition for UserQueryform."""

        model = UserQuery
        fields = ['to', 'query']
        

