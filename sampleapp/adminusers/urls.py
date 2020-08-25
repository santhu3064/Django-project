from django.conf.urls import include
from django.conf.urls import url
from adminusers import views


app_name = 'adminusers'

urlpatterns  = [
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
]