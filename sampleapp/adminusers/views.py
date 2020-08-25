from django.shortcuts import render
from adminusers import forms


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
