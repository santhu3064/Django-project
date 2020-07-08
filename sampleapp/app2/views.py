from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def index(request):
    data= {'firstname':'venkata lakshmi','lastname':'ruttala','age': '53','img':'mom'}
    return render(request,'app2/index.html',context={'data': data})