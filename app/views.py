from django.shortcuts import render

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(http_method_names=["GET", 'POST'])
def doctor_list_create_api_view(request):
    if request.method == "GET":
        doctors = models.Doctor.objects.all()
        serializer = serializers.DoctorSerializer(instance=doctors, many=True)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        received_data = request.data
        serializer = serializers.DoctorSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
