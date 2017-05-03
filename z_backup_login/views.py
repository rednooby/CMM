from django.shortcuts import render, redirect
from . import urls
#from .forms import JoinForm
from . models import join

# Create your views here.
def login(request):
	return render(request, 'login/login.html')

def join_new(request):
	if request.method == 'POST':
		form = JoinForm(request.POST)
		if form.is_valid(): #is_valid()함수는 유효성 검사. 즉 참일경우는 유효성검사 통과
 							#clean, cleaned는 유효성검사, 값변경 둘다 수행
 			join = form.save()
#			return redirect('login/login.html')
	else:
		form = JoinForm()
	return render(request, 'login/join.html',{'form' : form})
