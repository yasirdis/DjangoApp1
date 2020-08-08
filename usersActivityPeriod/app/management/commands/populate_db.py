from django.core.management.base import BaseCommand, CommandError
from app.models import Members, Activity_periods
from faker import Faker
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    #args = '<foo bar ...>'
    help = 'our help string comes here'
    def add_arguments(self,parser):
        pass

    def _create_member(self):
        fake = Faker() # used to generate fake data
        unique_id = get_random_string(length=9) # used to generate random unique id of 9 characters
        while (Members.objects.filter(id=unique_id).exists()):# checks againist availablity of unique id inside models
            unique_id = get_random_string(length=9)
        newmem = Members(id=unique_id,real_name=fake.name(),tz=fake.timezone())
        newmem.save()
        dateTime = fake.date()
        starttime = fake.time()
        endtime = fake.time()
        newAP = Activity_periods.objects.create(member_id=unique_id,start_time=dateTime+" "+starttime+fake.am_pm(),end_time=dateTime+" "+endtime+fake.am_pm())
        newAP.save() # stores fake data in activity
        dateTime2 = fake.date()
        starttime2 = fake.time()
        endtime2 = fake.time()
        newAP = Activity_periods.objects.create(member_id=unique_id,start_time=dateTime2+" "+starttime2+fake.am_pm(),end_time=dateTime2+" "+endtime2+fake.am_pm())
        newAP.save() #stores fake data for activite periods model 

    def handle(self, *args, **options):
        self._create_member()
