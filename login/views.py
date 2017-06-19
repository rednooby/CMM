from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

from .models import ActList, MyUser, BankBook
from .forms import ActListForm, BankBookForm
from django.db.models import Sum

# Create your views here.
def login(request):
	return render(request, 'login/login.html')


##메인화면##	/index/$
def index(request):
	qs_li = ActList.objects.filter(act__email=request.user.email)

	return render(request, 'login/index.html',{'qs_li': qs_li})


##통장 사용정보 출력##	/index/my_view/id/$
def my_list(request, id): #ActList의 id
	qs = ActList.objects.filter(act__email=request.user.email, id=id)
	qs_info = BankBook.objects.filter(name_id=id) #가장 최근날짜 최상위로 필터링 추가하기
	qs_li = ActList.objects.filter(act__email=request.user.email)
	
	qs_total = BankBook.objects.filter(name_id=id).aggregate(Sum('act_total'))

	

	print(qs_total)
	return render(request, 'login/my_list.html', {'qs': qs, 'qs_info':qs_info, 'qs_li':qs_li, 'qs_total':qs_total})


##통장 사용정보 출력##	/index/view/id/$
def my_view(request, id): #BankBook의 id
	qs_li = ActList.objects.filter(act__email=request.user.email)
	qs_info = BankBook.objects.filter(name=id) #가장 최근날짜 최상위로 필터링 추가하기
	qs_view = BankBook.objects.filter(id=id) 

	print(qs_info)
	return render(request, 'login/my_view.html', {'qs_info':qs_info, 'qs_li':qs_li, 'qs_view':qs_view})


##통장 사용정보 수정##	/index/edit/id/$
def my_edit(request, id):
	bankbook = get_object_or_404(BankBook, id=id)

	if request.method == 'POST':
		form = BankBookForm(request.POST, instance=bankbook)
		if form.is_valid():
			bankbook = form.save()

			return redirect('/index/edit/{}'.format(id))
	else:
		form = BankBookForm(instance=bankbook)

	#qs = ActList.objects.filter(act__email=request.user.email, id=id)
	qs_li = ActList.objects.filter(act__email=request.user.email)
	
	print(form)
	return render(request, 'login/my_edit.html', {'form': form, 'qs_li':qs_li})


##통장 사용정보 삭제##
def my_delete(request, id):
	bankbook = get_object_or_404(BankBook, id=id)

	bankbook = BankBook.objects.get(id=id)
	bankbook.delete()

	return redirect('login:index')


##계좌에 금액추가##	/id/$
def bankbook_new(request, id):
	if request.method == 'POST':
		form = BankBookForm(request.POST)
		if form.is_valid():
			bankbook = form.save(commit=False)
			bankbook.name = request.user.actlist_set.all().get(id=id)
			#bankbook.name = request.user.actlist_set.filter(act_name=act_name)
			#안되는 이유=>쿼리셋은 다수의 모델필드를 DB에 쿼리하기 위한 객체. 그래서 직접 모델필드로 담을수 없음
			#request.user.actlist_set.filter는 쿼리셋인데 외래키 필드에 지정하여 오류가 난것
			
			if bankbook.act_part == "수입":
				bankbook.act_total += bankbook.act_price
			else:
				bankbook.act_total -= bankbook.act_price
			
			bankbook.save()

			return redirect('index')
	


	else:
		form = BankBookForm()

	qs = ActList.objects.filter(act__email=request.user.email, id=id)
	qs_li = ActList.objects.filter(act__email=request.user.email)

	
	#print(form)
	return render(request, 'login/bankbook.html', {'form': form, 'qs':qs, 'qs_li':qs_li})
	#_set의 사용: 어떤 model에서 자신을 foreign key로 가지고 있는 모델이 접근하기 위해 Manager를 이용할때 사용
	#set 정보: http://freeprog.tistory.com/55


'''
##계좌에 금액추가##	/id/$
def bankbook_new(request, id):
	if request.method == 'POST':
		form = BankBookForm(request.POST)
		if form.is_valid():
			bankbook = form.save(commit=False)
			bankbook.name = request.user.actlist_set.all().get(id=id)
			
			#bankbook.name = request.user.actlist_set.filter(act_name=act_name)
			#안되는 이유=>쿼리셋은 다수의 모델필드를 DB에 쿼리하기 위한 객체. 그래서 직접 모델필드로 담을수 없음
			#request.user.actlist_set.filter는 쿼리셋인데 외래키 필드에 지정하여 오류가 난것
			bankbook.save()

			return redirect('index')
	else:
		form = BankBookForm()

	qs = ActList.objects.filter(act__email=request.user.email, id=id)
	qs_li = ActList.objects.filter(act__email=request.user.email)
	
	#print(form)
	return render(request, 'login/bankbook.html', {'form': form, 'qs':qs, 'qs_li':qs_li})
	#_set의 사용: 어떤 model에서 자신을 foreign key로 가지고 있는 모델이 접근하기 위해 Manager를 이용할때 사용
	#set 정보: http://freeprog.tistory.com/55
'''

##회원가입##	/join/$
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


'''
def bankbook_list(request, act_name):
	qs = ActList.objects.filter(act__email=request.user.email, act_name=act_name)
	qs_li = ActList.objects.filter(act__email=request.user.email)

	print()


	return render(request, 'account_info',{
		'qs': qs, 'qs_li': qs_li
		})
'''




@login_required
##통장정보 출력##	/mypage/act_name/$
def account_info(request, act_name):
	qs = ActList.objects.filter(act__email=request.user.email, act_name=act_name)
	qs_li = ActList.objects.filter(act__email=request.user.email)

	print()


	return render(request, 'login/account_info.html',{
		'qs': qs, 'qs_li': qs_li
		})


##회원정보, 통장정보 출력(mypage)##	/mypage/$
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
 

##통장정보 수정 (아직 안된것 수정해야됨)##		/mypage/act_name/edit/$
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