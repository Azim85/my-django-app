import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker
fakegen = Faker()

topic_list = ['Programming', 'GameDev', 'HR', 'Movie','Sport']
from random import choice

def add_topic():

    t = Topic.objects.get_or_create(top_name=choice(topic_list))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        top = add_topic()    

        fake_company_name = fakegen.company()
        fake_url_name = fakegen.url()
        fake_date = fakegen.date()

        webpage = Webpage.objects.get_or_create(topic=top, name=fake_company_name, url=fake_url_name)[0]

        acc = AccessRecord.objects.get_or_create(name=webpage, date = fake_date)[0]

if __name__ == '__main__':
    print('Populating')
    populate(10)
    print('completed')        
