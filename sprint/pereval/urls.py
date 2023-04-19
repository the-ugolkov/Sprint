from django.urls import path
from .views import submit_data, get_data, update_pereval

urlpatterns = [
    path('submitData/', submit_data, name='submit_data'),
    path('submitData/<int:pk>/', get_data, name='get_data'),
    path('submitData/<int:pk>/update/', update_pereval, name='update_data'),
]
