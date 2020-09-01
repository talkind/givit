from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField()
    date_of_birth = forms.CharField(max_length=100)
    home_address = forms.CharField(max_length=100)
    field_of_study = forms.CharField(max_length=100)
    degree = forms.CharField(max_length=100)
    scholarship = forms.CharField(max_length=100)
    membership_type = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            'password1',
            'password2',
            'email',
            'phone_number',
            'date_of_birth',
            'home_address',
            "field_of_study",
            'degree',
            'scholarship',
            'membership_type'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.home_address = self.cleaned_data['home_address']
        user.field_of_study = self.cleaned_data['field_of_study']
        user.degree = self.cleaned_data['degree']
        user.scholarship = self.cleaned_data['scholarship']
        user.membership_type = self.cleaned_data['membership_type']

        if commit:
            user.save()

        return user
