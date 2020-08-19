from django.shortcuts import render


# Create your views here.


def index(request):
    test = {"name": "Venkata Lakshmi", "age": 53}
    return render(request, 'relativetemplatingapp/index.html',
                  context={'test': test})


def sample(request):
    return render(request, 'relativetemplatingapp/sample.html')


def other(request):
    return render(request, 'relativetemplatingapp/other.html')
