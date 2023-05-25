from django.shortcuts import render


from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from . import models
from . import serializers
from . import my_generic


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


@api_view(http_method_names=["GET", "POST"])
def patient_list_create_api_view(request):
    if request.method == "GET":
        patients = models.Patient.objects.all()
        serializer = serializers.PatientSerializer(instance=patients, many=True)
        return Response(serializer.data, status=200)
    if request.method == "POST":
        serializer = serializers.PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


# @api_view(http_method_names=["GET", "PUT", "DELETE"])
# def patient_retrieve_update_destroy_api_view(request, pk):
#     patient = get_object_or_404(models.Patient, pk=pk)
#
#     if request.method == "GET":
#         serializer = serializers.PatientSerializer(instance=patient)
#         return Response(serializer.data)
#
#     if request.method == "PUT":
#         serializer = serializers.PatientSerializer(instance=patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)
#
#     if request.method == "DELETE":
#         patient.delete()
#         return Response(status=204)


class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class PatientRetrieveUpdateDestroyAPIView(my_generic.MyGenericRetrieveUpdateDestroyAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
