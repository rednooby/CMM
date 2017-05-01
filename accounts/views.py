from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('signup_form.html')
	else:
		form = UserCreationForm()

	return render(request, 'accounts/signup_form.html',{'form' : form})