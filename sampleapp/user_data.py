import os
import django
from faker import Faker
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sampleapp.settings')

django.setup()

from users.models import Users

fake = Faker()

def load_users(n):

    for i in range(n):
        first_name= fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        user = Users.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)
        # user.save()



if __name__ == '__main__':

    print("Loading users")
    load_users(30)