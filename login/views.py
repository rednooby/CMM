from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

from .models import ActList, MyUser, BankBook
from .forms import ActListForm, BankBookForm

# Create your views here.
def login(request):
	return render(request, 'login/login.html')


def index(request):
	qs = ActList.objects.filter(act__email=request.user.email)

	print(qs)
	return render(request, 'login/index.html',{'qs': qs})


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

def bankbook_list(request, act_name):
	qs = ActList.objects.filter(act__email=request.user.email, act_name=act_name)
	qs1 = ActList.objects.filter(act__email=request.user.email)

	print()


	return render(request, 'login/account_info.html',{
		'account_info': qs, 'actlist': qs1
		})

def bankbook_new(request, act_name):
	if request.method == 'POST':
		form = BankBookForm(request.POST)
		if form.is_valid():
			bankbook = form.save(commit=False)
			bankbook.name = request.user.actlist_set.filter(act_name=act_name)
			bankbook.save()

			return redirect('index')
	else:
		form = BankBookForm()

	qs = ActList.objects.filter(act__email=request.user.email, act_name=act_name)
	qs1 = BankBook.objects.all()
	
	#qs1 = BankBook.objects.filter(name__act_name=request.user.actlist_set.all())
	print(qs)
	return render(request, 'login/bankbook.html', {'form': form, 'qs':qs, 'qs1':qs1})
	#_set의 사용: 어떤 model에서 자신을 foreign key로 가지고 있는 모델이 접근하기 위해 Manager를 이용할때 사용
	#set 정보: http://freeprog.tistory.com/55


@login_required
##통장정보 출력##
def account_info(request, act_name):
	qs = ActList.objects.filter(act__email=request.user.email, act_name=act_name)
	qs1 = ActList.objects.filter(act__email=request.user.email)

	print()


	return render(request, 'login/account_info.html',{
		'account_info': qs, 'actlist': qs1
		})


#목록, 데이터 입력
@login_required
def Managment(request):
	if request.method == 'POST':
		form = ActListForm(request.POST) #파일이 있으면 request.FILES도 추가
		if form.is_valid():#여기서 폼의 역할은 끝남
			act_list = form.save(commit=False)
			act_list.act = request.user
			act_list.save()
			#form.cleaned_data #검증을 끝마친 데이터를 form으로
			
			#val = ActList(**self.cleaned_data)#검증 마친 데이터를 val로
			#val.save()#결국은 저장

			return redirect('Managment')
			#return redirect(val)
	else:
		form = ActListForm()#GET으로 들어오면 Forms.py의 ActListForm을 출력
		print(form)
	##자신의 계좌만 필터링##	
	qs = ActList.objects.filter(act__email=request.user.email)
	#print(act) #쿼리셋 검증

	return render(request, 'login/mypage.html', {'Managment': qs, 'form': form}) 
 

#데이터 수정 (아직 안된것 수정해야됨)
def account_edit(request, act_name):
	act_list = get_object_or_404(ActList, act_name=act_name)

	if request.method == 'POST':
		form = ActListForm(request.POST, instance=act_list)
		if form.is_valid():
			act_list = form.save(commit=False)
			act_list.act = request.user
			act_list.save()
			
			return redirect('Managment')
			#return redirect(val)
	else:
		form = ActListForm(instance=act_list)
		print(form)
	##자신의 계좌만 필터링##	
	qs = ActList.objects.filter(act__email=request.user.email)
	#print(act) #쿼리셋 검증
	return render(request, 'login/mypage.html', {'Managment': qs, 'form': form}) 


def UserChangeForm(request):
	user = request.user
	form = updateMemberForm(request.POST)

	if request.method == 'POST':
		if form.is_valid():

			user.birth = request.POST['birth']
			user.nickname = request.POST['nickname']

			user.save()
			return redirect(settings.UPDATE_URL)