from django.shortcuts import render
from adminusers import forms


# Create your views here.

def index(request):
    return render(request, 'adminusers/index.html')


def register(request):
    user_form = forms.Userform()
    profile_form = forms.profile_form()
    registered = False
    if request.method == 'POST':
        user_form = forms.Userform(data=request.POST)
        profile_form = forms.profile_form(data=request.POST)

    return render(request, 'adminusers/register.html')
