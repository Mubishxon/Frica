from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Parol",
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Parol takrorlang",
                               widget=forms.PasswordInput)
    class Meta:
        fields = ('username', 'first_name', 'email')

    def clean_password_2(self):
        data = self.cleaned_data
        if data["password"] != data["password_2"]:
            raise forms.ValidationError("ikkala parolingiz ham bir bitiga teng bolishi kerak")
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'date_of_birth']