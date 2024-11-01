# from django.urls import path
#
# urlpatterns = [
#     # TODO: зарегистрируйте необходимые маршруты
# ]

# measurement/urls.py
from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateDestroyView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateDestroyView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]
