from http.client import HTTPResponse
import json
from urllib import request
from django.shortcuts import render, HttpResponse
from zssn_app.models import Survivors
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Survivors
from . serializers import SurvivorsSerializer
from . serializers import SurvivorsSerializerLocation

# Create your views here.
def index(request):
    return HttpResponse("Hello, <br><br> GoTo <b>'/survivors'</b> to return Return all survivors in ZSSN <br>"
    "<br> GoTo <b>'/post'</b> to Creates a new survivor in ZSSN <br>"
    "<br> GoTo <b>'/put'</b> to Updates a survivor's location in ZSSN <br>"
    "<br> GoTo <b>'/survivors/reports'</b> to Reports the percentage of infected and non infected users in ZSSN")

def post(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        infected = request.POST.get('infected')
        survivors = Survivors(name=name, age=age, gender=gender, latitude=latitude, longitude=longitude, infected=infected)
        survivors.save()
    return render(request, 'new_survivor.html')



class SurvivorsList(APIView):

    def get(self, request):
        survivor1 = Survivors.objects.all()
        serializer = SurvivorsSerializer(survivor1, many=True)

        return Response(serializer.data)

    # def post(self):
    #     serializer = SurvivorsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        survivor2 = Survivors.objects.filter(id=id)
        serializer2 = SurvivorsSerializerLocation(survivor2, data=request.data)

        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

class SurvivorListInfected(APIView):

    def get(self, request):
        survivor1 = Survivors.objects.filter(infected=True)
        # serializer = SurvivorsSerializer(survivor1, many=True)

        total_count = Survivors.objects.all().count()
        infection_count = Survivors.objects.filter(infected=True).count()
        infection_percent = str(round((infection_count*100)/total_count, 3)) + ' %'

        data1 = {'Total Survivors': total_count, 'Infected Survivors': infection_count, 'Percentage of infection among survivors': infection_percent}

        # return Response(serializer.data)
        return HttpResponse(json.dumps(data1))

