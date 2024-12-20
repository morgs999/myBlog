# blog/forms.py

from django import forms

class ExampleSignupForm(forms.Form):
    """example form"""
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField()
    gender = forms.ChoiceField(
        label='Gender',
        required=False,
        choices=[
            (None, '-------'),
            ('m', 'Male'),
            ('f', 'Female'),
            ('n', 'Non-binary'),
        ]
    )
    receive_newsletter = forms.BooleanField(
        required=False,
        label='Do you wish to receive our newsletter?'
    )

class PhotoContestForm(forms.Form):
    """photo contest form"""
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=True)
