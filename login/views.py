from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
	return render(request, 'login/login.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('signup_form.html')
	else:
		form = UserCreationForm()

	return render(request, 'login/signup_form.html',{'form' : form})