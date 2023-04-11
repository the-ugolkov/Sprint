from rest_framework.serializers import ModelSerializer

from pereval.models import Users, PerevalAdded, Coords, PerevalImages, PerevalAreas


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalAddedSerializer(ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalImagesSerializer(ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'


class PerevalAreasSerializer(ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = '__all__'
