from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse(u"欢迎光临，自强学堂！")
def home(request):
	string = u'学习Django，建立一个测试管理平台！'
	TutorialList=['HTML','CSS','Javsscript','Linux','Django']
	info_dict = {'site':u'自强学堂','content':u'学习各种web技术'}
	return render(request,'home.html',{'info_dict':info_dict})