from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email =  models.EmailField(max_length=100)

    def __str__(self):
        return self.email
