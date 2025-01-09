from rest_framework import serializers
from .models import Sensor, Measurement

class Measurement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class Sensor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class Sensor_Detail_Serializer(serializers.ModelSerializer):
    measurements = Measurement_Serializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
