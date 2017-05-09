from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required #장식자로 로그인 되었을때만 페이지를 표시한다
def index(request):
	print(request.user, 'has login') #유저 로그에 남기기
	return render(request, 'main/index.html')