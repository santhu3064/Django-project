from django.shortcuts import render

from signup import forms


# Create your views here.

def index(request):
    return render(request, 'signup/index.html')


def signupform(request):
    form = forms.Signup()
    if request.method == 'POST':
        form = forms.Signup(request.POST)

        if form.is_valid():
            print("{},{},{}".format(form.cleaned_data['name'],
                                    form.cleaned_data['email'],
                                    form.cleaned_data['comments']))
    return render(request, 'signup/signup.html', {'form': form})
