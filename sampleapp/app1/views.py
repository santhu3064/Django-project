from django.shortcuts import render
from app1.models import Topic
from app1.models import AccessRecord


# Create your views here.

from django.http import HttpResponse

def index(request):
    data= {'firstname':'venkata lakshmi','lastname':'ruttala','age': '53','img':'mom'}
    return render(request,'app2/index.html',context={'data': data})

#
# def get_topics(request):
#     topics = Topic.objects.all()
#
#     return  render(request,'app1/sample.html',context={'topics': topics})


def get_access_records(request):
    accessrecords = AccessRecord.objects.all()
    print("{}".format(accessrecords))

    return render(request, 'app1/sample.html', context={'accessrecords': accessrecords})