from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('profile', user_id=user.id)
		else:
			# Handle invalid login credentials
			pass
	else:
		# Render the login form
		pass
