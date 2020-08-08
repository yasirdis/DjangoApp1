from django.db import models

# Create your models here.

class Members(models.Model):#contains all members
    id =models.CharField(primary_key = True,max_length = 20)
    real_name = models.CharField(max_length = 20)
    tz = models.CharField(max_length = 20)
    def __str__(self):
        return self.id
class Activity_periods(models.Model):#contains all activites of members
    #Feb 1 2020  1:33PM
    member = models.ForeignKey(Members,related_name='activity_periods', on_delete = models.CASCADE) # refers to member instance
    start_time = models.CharField(max_length = 20)
    end_time = models.CharField(max_length = 20)
