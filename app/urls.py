from django.urls import path
from . import views


urlpatterns = [
    path('doctors/', views.doctor_list_create_api_view),
    path('patients/', views.patient_list_create_api_view),

    path('patients/<int:pk>', views.patient_retrieve_update_destroy_api_view),
]
