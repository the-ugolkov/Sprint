from django_filters import rest_framework as filters
from .models import PerevalAdded

class PerevalFilter(filters.FilterSet):
    user__email = filters.CharFilter(field_name='user__email')

    class Meta:
        model = PerevalAdded
        fields = ['user__email']