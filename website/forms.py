#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
	#	fields = ['firstname','lastname',  'email','telephone', 'password1', 'password2']
		fields = ['username',  'email', 'password1', 'password2']