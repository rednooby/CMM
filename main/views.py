from django.shortcuts import render

# Create your views here.

def index(request):
	print(request.user, 'has login') #유저 로그에 남기기
	return render(request, 'main/index.html')

def login(request):
	return render(request, 'login/login.html')