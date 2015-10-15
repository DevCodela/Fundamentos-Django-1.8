# encoding=utf-8
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):

	username = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
							'type' : 'text',
							'placeholder' : 'Ingresa un nombre de usuario'
						}))
	password = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
							'type' : 'password',
							'placeholder' : 'Ingresa una contraseña'
						}))

	def clean(self):
		user_exist = User.objects.filter(username = self.cleaned_data['username'])
		if not user_exist:
			self.add_error('username', 'El nombre de usuario no existe!')
		else:
			user = User.objects.get(username = self.cleaned_data['username'])
			if not user.check_password(self.cleaned_data['password']):
				self.add_error('password', 'El password es incorrecto')






