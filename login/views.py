from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

from .models import ActList, MyUser

# Create your views here.
def login(request):
	return render(request, 'login/login.html')


def join(request):
	print(request.user) #유저 로그에 남기기
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): #유효성 검사 수행 여기서 forms.py의 def save로 가서 검사하는듯. 거기 주석하고 실행하면 여기서 에러남
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = UserCreationForm()

	return render(request, 'login/join.html',{'form' : form})


@login_required
def Managment(request):
	qs = ActList.objects.filter(actId__email=request.user.email)
	print(qs)
	return render(request, 'login/mypage.html', {
		'Managment': qs,}) 


##통장정보 출력##
def AccountInfo(request, actName):
	qs = ActList.objects.filter(actId__email=request.user.email, actName=actName)
	print(actName)
	return render(request, 'login/accountInfo.html',{
		'AccountInfo': qs,
		}) 


def UserChangeForm(request):
	user = request.user
	form = updateMemberForm(request.POST)

	if request.method == 'POST':
		if form.is_valid():

			user.birth = request.POST['birth']
			user.nickname = request.POST['nickname']

			user.save()
			return redirect(settings.UPDATE_URL)