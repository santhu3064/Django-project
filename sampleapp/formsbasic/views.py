from django.shortcuts import render

from formsbasic import forms


# Create your views here.

def index(request):
    return render(request, 'formsbasic/index.html')


def signupform(request):
    form = forms.Signup()
    if request.method == 'POST':
        form = forms.Signup(request.POST)

        if form.is_valid():
            print(
                "{},{},{}".format(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['comments']))
    return render(request, 'formsbasic/basicform.html', {'form': form})
