# measurement/views.py
from rest_framework import generics
from measurement.models import Sensor, Measurement 
from .serializers import Sensor_Serializer, Measurement_Serializer, Sensor_Detail_Serializer

# Создать и получить список датчиков
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = Sensor_Serializer


# Получить, изменить и удалить конкретный датчик
class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = Sensor_Detail_Serializer


# Создать новое измерение
class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = Measurement_Serializer

   def perform_create(self, serializer):
        try:
            sensor = Sensor.objects.get(id=self.request.data['sensor'])  # Проверка существования сенсора
        except Sensor.DoesNotExist:
            raise serializers.ValidationError("Sensor with this ID does not exist.")  # Ошибка, если сенсор не найден
        serializer.save(sensor=sensor)
