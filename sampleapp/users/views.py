from django.shortcuts import render
from users.models import Users

# Create your views here.


def index(request):
    users = Users.objects.all()
    return render(request, 'users/index.html',context={'users':users} )