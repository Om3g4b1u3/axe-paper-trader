from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=32)
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

