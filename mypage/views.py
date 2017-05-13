from django.shortcuts import render

# Create your views here.

def managment(request):
	return render(request, 'mypage/mypage.html') 
