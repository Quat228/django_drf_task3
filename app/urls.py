from django.urls import path
from . import views


urlpatterns = [
    path('doctors/', views.doctor_list_create_api_view),
    path('patients/', views.PatientListCreateAPIView.as_view()),
]
