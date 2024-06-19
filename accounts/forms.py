from django import forms
from .models import User, Lab

class CommonForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'aadhar', 'address', 'username', 'password']

    def clean(self):
        cleaned_data = super(CommonForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LabExtraForm(forms.ModelForm):
    """Form definition for LabExtra."""

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    class Meta:
        """Meta definition for LabExtraform."""

        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super(LabExtraForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class LabForm(forms.ModelForm):
    """Form definition for Lab."""

    class Meta:
        """Meta definition for Labform."""

        model = Lab
        exclude = ('owner',)


class CForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'username', 'password']

    def clean(self):
        cleaned_data = super(CForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )