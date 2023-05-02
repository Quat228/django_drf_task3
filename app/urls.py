from django.urls import path
from . import views


urlpatterns = [
    path('doctors/', views.doctor_list_create_api_view),
    path('patients/', views.patient_list_create_api_view),

    path('doctors/<int:pk>', views.DoctorRetrieveUpdateDestroyAPIView.as_view()),
    path('patients/<int:pk>', views.PatientRetrieveUpdateDestroyAPIView.as_view()),
]
