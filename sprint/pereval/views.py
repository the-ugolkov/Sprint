from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from pereval.models import PerevalAdded
from pereval.serializers import PerevalAddedSerializer


class PerevalViewSet(ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

