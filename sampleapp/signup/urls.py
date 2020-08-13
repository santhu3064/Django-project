from django.conf.urls import url

from signup import views

urlpatterns = [
    url(r'^$', views.index, name='formindex'),
    url(r'^$', views.index, name='formform'),
]
