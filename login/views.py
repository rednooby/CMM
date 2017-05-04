from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
	return render(request, 'login/login.html')

def join(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): #유효성 검사 수행
			form.save()
			return redirect(login)
	else:
		form = UserCreationForm()

	return render(request, 'login/join.html',{'form' : form})