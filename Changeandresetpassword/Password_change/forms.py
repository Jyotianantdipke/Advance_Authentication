from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError((f"{value} is Registered already."), params={'value': value})


class UserForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

        def save(self, commit=True):
            user = super(UserForm, self).save(commit=False)
            user.email = self.cleaned_data.get("email")
            if commit:
                user.save()
            return user
