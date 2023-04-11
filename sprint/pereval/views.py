from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pereval.models import PerevalAdded
from pereval.serializers import PerevalAddedSerializer


class PerevalViewSet(ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalAddedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
