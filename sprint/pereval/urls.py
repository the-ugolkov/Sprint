from django.urls import path
from .views import submit_data, get_data

urlpatterns = [
    path('submitData/', submit_data, name='submit_data'),
    path('submitData/<int:pk>/', get_data, name='get_data'),
]