from django.contrib import admin

# Register your models here.

from adminusers.models import UserProfileInfo

admin.site.register(UserProfileInfo)