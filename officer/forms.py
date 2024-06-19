from django import forms
from .models import Crops, Fertilizer, Pesticide, Seminar, Irrigation, Scheme
from accounts.models import Lab, User
from user.models import UserQuery

class CropsForm(forms.ModelForm):
    """Form definition for Crops."""

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        """Meta definition for Cropsform."""

        model = Crops
        fields = '__all__'

class PesticideForm(forms.ModelForm):
    """Form definition for Pesticide."""

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        """Meta definition for Pesticideform."""

        model = Pesticide
        fields = '__all__'

class FertilizerForm(forms.ModelForm):
    """Form definition for Fertilizer."""

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        """Meta definition for Fertilizerform."""

        model = Fertilizer
        fields = '__all__'

class IrrigationForm(forms.ModelForm):
    """Form definition for Irrigation."""

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        """Meta definition for Irrigationform."""

        model = Irrigation
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class SeminarForm(forms.ModelForm):
    """Form definition for Seminar."""

    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput(
        attrs={'min': '07:00', 'max':'17:00'}
    ))
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        """Meta definition for Seminarform."""

        model = Seminar
        fields = '__all__'


class SchemeForm(forms.ModelForm):
    """Form definition for GovernmentSchemes."""

    class Meta:
        """Meta definition for GovernmentSchemesform."""

        model = Scheme
        fields = "__all__"

class QueryReplyForm(forms.ModelForm):
    """Form definition for Queryreply."""

    class Meta:
        """Meta definition for Queryreplyform."""

        model = UserQuery
        fields = ('reply',)







