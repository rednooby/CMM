from django.shortcuts import render, redirect
from .forms import UserCreationForm
#from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
	return render(request, 'login/login.html')

def join(request):
	print(request.user) #유저 로그에 남기기
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): #유효성 검사 수행 여기서 forms.py의 def save로 가서 검사하는듯. 거기 주석하고 실행하면 여기서 에러남
			form.save()
			return redirect(login)
	else:
		form = UserCreationForm()

	return render(request, 'login/join.html',{'form' : form})