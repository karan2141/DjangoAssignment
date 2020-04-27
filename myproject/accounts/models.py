from django.db import models
from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user donot exist register this user first')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address', required=True)
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords are not equal')
        password_validation.validate_password(self.cleaned_data.get('password'), None)
        return self.cleaned_data

    def cleanEmail(self):
        email = self.cleaned_data.get('email')
        email_in = User.objects.filter(email=email)
        if email_in.exists():
            raise forms.ValidationError("email already registered")
        return email