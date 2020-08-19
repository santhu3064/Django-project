"""sampleapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from app1 import views
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from signup import views as from_views
from users import views as users_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^app2/', include('app2.urls')),
    url(r'^app1/', include('app1.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^index/', from_views.index, name='signupindex'),
    url(r'^signup/', from_views.signupform, name='signup'),
    url(r'^users/signup/', users_views.users, name='usersignup'),
    # url(r'^template/',template_views.index, name='template_index'),
    url(r'^templates/',include('relativetemplatingapp.urls')),
]
