from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm

def login(request):
	form = LoginForm()
	return render(request, 'login.html', {'form': form})

@login_required
def profile(request, user_id):
	user = User.objects.get(id=user_id)
	# Retrieve any additional data for the user's profile as needed
	context = {
		'user': user,
		# Add any additional context data needed for the profile page
	}
	return render(request, 'profile.html', context)
