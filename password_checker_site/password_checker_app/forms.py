from django import forms

class PasswordCheckerForm(forms.Form):
    pw_input=forms.CharField(
        required=True,
        label='',
    )