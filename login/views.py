from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

from .models import ActList, MyUser, BankBook, ActBoard
from django.db.models import Sum
from django.views.generic import ListView, DetailView, TemplateView
#페이징
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

def test(request):
	return render(request, 'login/test.html')


# Create your views here.
def login(request):
	return render(request, 'login/login.html')


##메인화면##	/index/$
def index(request):
	qs_li = ActList.objects.filter(act__email=request.user.email)
	qs_graph_up = BankBook.objects.all().order_by('act_total')[0]#가장큰 수입
	qs_graph_down = BankBook.objects.all().order_by('-act_total')[0]#가장큰 지출
	#qs_income = BankBook.objects.filter(act_payment='수입').order_by('-act_price')#전체 수입 목록
	#qs_expenses = BankBook.objects.filter(act_payment='지출').order_by('-act_price')#전체 지출 목록

	qs_income_all = BankBook.objects.filter(act_content='적금').order_by('-act_price')#저축 랭킹
	qs_food_all = BankBook.objects.filter(act_content='식비').order_by('-act_price')#저축 랭킹
	qs_expenses_all = BankBook.objects.filter(act_content='여가비').order_by('-act_price')#지출 전체 출력

	return render(request, 'login/index.html',{'qs_li': qs_li, 'qs_graph':qs_graph_up, 'qs_graph_down':qs_graph_down, 'qs_income_all': qs_income_all, 'qs_expenses_all': qs_expenses_all, 'qs_food_all':qs_food_all})


##게시판 리스트 /board/list
def board_list(request):
	qs_li = ActList.objects.filter(act__email=request.user.email)#메뉴 통장 출력	return render(request, 'login/board_list.html', {'qs_li' : qs_li})
	
	qs_board_list = ActBoard.objects.all().order_by('-id')

	paginator = Paginator(qs_board_list, 5)
	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	return render(request, 'login/board_list.html', {'contacts': contacts, 'qs_li':qs_li,'qs_board_list':qs_board_list})

	
##게시판 글쓰기 /board/write
def board_write(request):
	if request.method == 'POST':
		form = ActBoardForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.board_name = request.user
			post.board_nick = request.user.nickname
			post.save()
		
			return redirect('login:board_list')

	else:
		form = ActBoardForm()

	print()
	qs_li = ActList.objects.filter(act__email=request.user.email)
	return render(request, 'login/board_write.html', {'form': form,'qs_li': qs_li})


##게시판 글읽기 /board/view/id
def board_view(request, id):
	
	qs_li = ActList.objects.filter(act__email=request.user.email)
	qs_board_view = ActBoard.objects.filter(id=id)

	return render(request, 'login/board_view.html',{'qs_li':qs_li, 'qs_board_view': qs_board_view})


##게시판 글수정 /board/edit/id
def board_edit(request,id):
	post = get_object_or_404(ActBoard, id=id)

	if request.method == 'POST':
			form = ActBoardForm(request.POST, instance=post)
			if form.is_valid():
				post.save()
			
				return redirect('/board/view/{}'.format(id))

	else:
		form = ActBoardForm(instance=post)


	qs_li = ActList.objects.filter(act__email=request.user.email)
	return render(request, 'login/board_edit.html',{'form': form,'qs_li': qs_li})


##게사판 글삭제/voard/delete/id
def board_delete(request, id):
	post = get_object_or_404(ActBoard, id=id)

	post = ActBoard.objects.get(id=id)
	post.delete()

	return redirect('/board/list')




##통장 사용정보 출력##	/index/my_list/id/$
def my_list(request, id): #ActList의 id
	qs = ActList.objects.filter(act__email=request.user.email, id=id)
	
	qs_info = BankBook.objects.filter(name_id=id).order_by('-act_date')

	qs_graph = BankBook.objects.filter(name_id=id).order_by('act_date')
	qs_income = BankBook.objects.filter(name_id=id, act_part="수입").order_by('act_date')#수입
	qs_expenses = BankBook.objects.filter(name_id=id,act_part="지출").order_by('act_date')#지출
	qs_li = ActList.objects.filter(act__email=request.user.email)
	
	qs_total = BankBook.objects.filter(name_id=id).aggregate(Sum('act_total'))
	qs_total_income = BankBook.objects.filter(name_id=id, act_part="수입").aggregate(Sum('act_total'))
	qs_total_expenses = BankBook.objects.filter(name_id=id, act_part="지출").aggregate(Sum('act_total'))

	qs_circle = BankBook.objects.filter(name_id=id,act_part="지출")
	print(qs_circle)

	return render(request, 'login/my_list.html', {'qs': qs, 'qs_info':qs_info, 'qs_li':qs_li, 'qs_total':qs_total, 'qs_income':qs_income, 'qs_expenses':qs_expenses, 'qs_graph':qs_graph, 'qs_total_income':qs_total_income, 'qs_total_expenses':qs_total_expenses, 'qs_circle':qs_circle})
	return HttpResponse(template.render(context))

##통장 사용정보 출력##	/index/my_view/id/$
def my_view(request, id): #BankBook의 id
	qs_li = ActList.objects.filter(act__email=request.user.email)
	qs_info = BankBook.objects.filter(name=id) #가장 최근날짜 최상위로 필터링 추가하기
	qs_view = BankBook.objects.filter(id=id) 

	print(qs_info)
	return render(request, 'login/my_view.html', {'qs_info':qs_info, 'qs_li':qs_li, 'qs_view':qs_view})


##통장 사용정보 수정##	/index/my_edit/id/$
def my_edit(request, id):
	bankbook = get_object_or_404(BankBook, id=id)

	if request.method == 'POST':
		form = BankBookForm(request.POST, instance=bankbook)
		if form.is_valid():
			bankbook = form.save()

			return redirect('/index/')
			return redirect('/index/my_list/{}'.format(id))
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

	qs = ActList.objects.filter(act__email=request.user.email, id=id)#통장이름입력 출력하기 위한 쿼리셋
	qs_li = ActList.objects.filter(act__email=request.user.email)

	
	#print(form)
	return render(request, 'login/bankbook.html', {'form': form, 'qs_li':qs_li, 'qs':qs})
	#_set의 사용: 어떤 model에서 자신을 foreign key로 가지고 있는 모델이 접근하기 위해 Manager를 이용할때 사용
	#set 정보: http://freeprog.tistory.com/55


##회원가입##	/join/$
def join(request):
	print(request.user) #유저 로그에 남기기
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid(): #유효성 검사 수행 여기서 forms.py의 def save로 가서 검사하는듯. 거기 주석하고 실행하면 여기서 에러남
			form.save()
			return redirect('login:login')
	else:
		form = UserCreationForm()

	return render(request, 'login/join.html',{'form' : form})


@login_required
##통장정보 출력##	/mypage/id/$
def account_view(request, id):
	qs_view = ActList.objects.filter(id=id)
	qs_li = ActList.objects.filter(act__email=request.user.email)

	print()


	return render(request, 'login/account_view.html',{
		'qs_view': qs_view, 'qs_li': qs_li
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

			return redirect('/mypage/')
			#return redirect(val)
	else:
		form = ActListForm()#GET으로 들어오면 Forms.py의 ActListForm을 출력
		print(form)
	##자신의 계좌만 필터링##	
	qs_li = ActList.objects.filter(act__email=request.user.email)
	#print(act) #쿼리셋 검증

	return render(request, 'login/mypage.html', {'qs_li': qs_li, 'form': form}) 
 

##통장정보 수정##		/mypage/id/edit/$
def account_edit(request, id):
	act_list = get_object_or_404(ActList, id=id)

	if request.method == 'POST':
		form = ActListForm(request.POST, instance=act_list)
		if form.is_valid():
			act_list.save()
			
			return redirect('/mypage/{}'.format(id))
	else:
		form = ActListForm(instance=act_list)
		print(form)

	qs_li = ActList.objects.filter(act__email=request.user.email)
	return render(request, 'login/account_edit.html', {'qs_li': qs_li, 'form': form}) 


##통장 삭제##
def account_delete(request, id):
	act_list = get_object_or_404(ActList, id=id)

	act_list = ActList.objects.get(id=id)
	act_list.delete()

	qs_view = ActList.objects.filter(id=id)
	qs_li = ActList.objects.filter(act__email=request.user.email)


	return redirect('/mypage/', {'qs_view':qs_view, 'qs_li':qs_li})


##이메일 찾기##		/searchemail/
class SearchEmail(TemplateView) :
    template_name = 'login/search_email.html'


# 사용자가 닉네임과 생년월일을 입력하고, myuser에 질의결과가 있으면 email 반환함. #
def find_username(request):
	if request.method == 'POST':
		form = FindUserNameForm(request.POST)
		nickname= request.POST.get('nickname')
		birth= request.POST.get('birth')
		if form.is_valid() and MyUser.objects.filter(nickname=nickname,birth=birth).exists():
			entry=MyUser.objects.filter(nickname=nickname)
			return render(request, 'login/search_email.html', {'Useremail': entry})
		else:
			return render(request, 'login/search_email.html', {'form':form})
	else:
		form = FindUserNameForm(request.POST)
		return render(request, 'login/search_email.html', {'form':form})


##비밀번호 찾기##	/searchpassword
class SearchPassword(TemplateView) :
    template_name = 'login/search_password.html'

# 이메일주소와 생년월일을 사용자가 입력하고, myuser에 질의한 결과가 있으면, pasword 변경하는 폼이 보임.#
def FindPassword(request):
	if request.method == 'POST':
		email= request.POST.get('email')
		birth= request.POST.get('birth')
		entry=MyUser.objects.filter(email=email, birth=birth)
		form = FindPasswordForm(request.POST)
		if form.is_valid() and entry.exists():
			entry=MyUser.objects.filter(email=email)
			return render(request, 'login/search_password.html', {'findpw': entry})
		else:
			return render(request, 'login/search_password.html', {'form':form})
	else:
		form = FindPasswordForm(request.POST)
		return render(request, 'login/search_password.html', {'form':form})


#비밀번호를 잊어벼렸을 경우 실행되는 view
#두번의 패스워드를 사용자가 입력하고 일치하면, 패스워드가 변경되면서 바로 login페이지로 이동한다.
def ForgetChangePw(request, email):
	if request.method == 'POST':
		form = ChangePwForm(request.POST)
		new_password1= request.POST.get('new_password1')
		new_password2= request.POST.get('new_password2')
		if form.is_valid() and new_password1 == new_password2:
			u = MyUser.objects.get(email__exact=email)
			u.set_password(new_password1)
			u.save()
			return redirect('login:login')
		else:
			return render(request, 'login/search_password.html', {'form':form})
	else:
		form = ChangePwForm(request.POST)
		return render(request, 'login/search_password.html', {})

#회원정보 페이지에 있는 비번변경 버튼을 누를경우 동작하는 view
def ChangePw(request):
	if request.method == 'POST':
		form = ChangePwForm(request.POST)
		new_password1= request.POST.get('new_password1')
		new_password2= request.POST.get('new_password2')
		if form.is_valid() and new_password1 == new_password2:
			u = MyUser.objects.get(email__exact=request.user.email)
			u.set_password(new_password1)
			u.save()
			return render(request, 'login/changepw.html', {})
		else:
			return render(request, 'login/changepw.html', {'form':form})
	else:
		form = ChangePwForm(request.POST)
		return render(request, 'login/changepw.html', {})


##회원정보 삭제
class DeleteConfirm(TemplateView) :
    template_name = 'login/my_delete_identification.html'

def delete_user(request):
	if request.method == 'POST':
		user = MyUser.objects.get(email=request.user.email)
		password= request.POST.get('password')
		form = DeleteUserForm(request.POST)
		if user.check_password(password):
			user.delete()
			return render(request, 'login/Withdrawal.html', {})
		else:
			return render(request, 'login/my_delete_identification.html', {})
	else:
		form = DeleteUserForm(email=request.user.email)
		return render(request, 'mypage/my_delete_identification.html', {})

