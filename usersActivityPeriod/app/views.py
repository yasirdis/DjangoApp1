from django.shortcuts import render
from app.models import Members, Activity_periods
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import MembersSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hello")

class MemberList(APIView):
    def get(self,request):# this method recieves request from user and returns DATA in the form of JSON
        member=Members.objects.all()#fetches all data from members model
        serializer = MembersSerializer(member,many=True)#converts member data with activity period data into Json
        return Response(serializer.data)#returns the respose to user
    def post(self):# thhis metod not used
        pass
