from django.conf.urls import url

from relativetemplatingapp import views

app_name = 'relativetemplatingapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sample/$', views.sample, name='sample'),
    url(r'^other/$', views.other, name='other'),
]
