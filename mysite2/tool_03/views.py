from django.shortcuts import render
from tool_03.models import  Blog

# Create your views here.
def index(request):
    a = Blog.objects.all().order_by('-id')[:5]
    return render(request, 'basemain.html',{'blogs':a})