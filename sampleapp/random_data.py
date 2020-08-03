import os
import django
from faker import Faker
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sampleapp.settings')

django.setup()

from app1.models import Topic, Webpage, AccessRecord

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    topic = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    topic.save()
    return topic


def populate(N):
    for i in range(N):
        topic = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        webpage = Webpage.objects.get_or_create(topic=topic,
                                                name=fake_name,
                                                url=fake_url)[0]
        accessrecord = AccessRecord.objects.get_or_create(name=webpage,
                                                          date=fake_date)[0]


if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Population complete")
