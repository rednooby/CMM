from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

from .models import ActList, MyUser
from .forms import ActListForm

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
	if request.method == 'POST':
		form = ActListForm(request.POST) #파일이 있으면 request.FILES도 추가
		if form.is_valid():#여기서 폼의 역할은 끝남
			form.save()
			#form.cleaned_data #검증을 끝마친 데이터를 form으로
			
			#val = ActList(**self.cleaned_data)#검증 마친 데이터를 val로
			#val.save()#결국은 저장

			return redirect('login/mypage.html')
			#return redirect(val)
	else:
		form = ActListForm()#GET으로 들어오면 Forms.py의 ActListForm을 출력

	##자신의 계좌만 필터링##	
	qs = ActList.objects.filter(actId__email=request.user.email)
	print(actId) #쿼리셋 검증

	return render(request, 'login/mypage.html', {'Managment': qs, 'form': form}) 


@login_required
##통장정보 출력##
def account_info(request, actName):
	qs = ActList.objects.filter(actId__email=request.user.email, actName=actName)
	print()

	return render(request, 'login/account_info.html',{
		'account_info': qs,
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