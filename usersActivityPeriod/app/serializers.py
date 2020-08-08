from rest_framework import serializers
from app.models import Members, Activity_periods

class APSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_periods
        fields= ['start_time','end_time']

class MembersSerializer(serializers.ModelSerializer):
    activity_periods = APSerializer(many=True, read_only=True)
    class Meta:
        model = Members
        fields= ['id','real_name','tz','activity_periods']
