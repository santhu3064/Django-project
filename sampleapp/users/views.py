from django.shortcuts import render
from users.models import Users
from users import forms


# Create your views here.


def index(request):
    users = Users.objects.all()
    return render(request, 'users/index.html', context={'users': users})


def users(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return 'Error Validating form'
    return render(request, 'users/signup.html', context={'form': form})
