from django.shortcuts import render
from adminusers import forms

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden


# Create your views here.

def index(request):
    return render(request, 'adminusers/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.Userform(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()

            registered = True

        else:
            print("USER ERROR: {} , PROFILE ERROR: {}".format(user_form.errors, profile_form.errors))
    else:
        user_form = forms.Userform()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'adminusers/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('adminusers:index'))
            else:
                return HttpResponseForbidden('User Not active.Contact adminstrator')
        else:
            print(username,password)
            return HttpResponse('User not found', status=404)
    else:
        return render(request, 'adminusers/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'adminusers/logout.html', {})
