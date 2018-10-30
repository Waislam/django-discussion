from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
	email =forms.CharField(widget=forms.EmailInput(), required=True, max_length=300)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

