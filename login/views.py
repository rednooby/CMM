from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
	return render(request, 'login/login.html')

def join(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('join.html')
	else:
		form = UserCreationForm()

	return render(request, 'login/join.html',{'form' : form})