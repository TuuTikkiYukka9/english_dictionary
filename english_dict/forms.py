from django import forms
from english_dict.models import PartProperty
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SelectWordForm(forms.Form):
    frequency = forms.BooleanField(label='Частотные', required=False)
    word_type = forms.ModelChoiceField(label='Тип слов', required=False, queryset=PartProperty.objects.all())


class TranslateForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea, required=False)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
