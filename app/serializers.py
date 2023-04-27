from rest_framework import serializers

from . import models


class DoctorSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=30)
    experience = serializers.IntegerField()

    def create(self, validated_data):
        return models.Doctor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'
