# measurement/views.py
from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

# Создать и получить список датчиков
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Получить, изменить и удалить конкретный датчик
class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Создать новое измерение
class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = Sensor.objects.get(id=self.request.data['sensor'])
        serializer.save(sensor=sensor)
