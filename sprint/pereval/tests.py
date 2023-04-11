from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PerevalAdded, Users, Coords, PerevalImages


class PerevalAddedTests(APITestCase):
    def setUp(self):
        self.url = reverse('submit_data')
        self.user = Users.objects.create(first_name='TestUser', last_name='TestUser', password='testpassword',
                                         email='123', otc='TestUser')  # Создаем тестового пользователя
        self.coord = Coords.objects.create(latitude=1.0, longitude=2.0, height=2.0)  # Создаем тестовые координаты
        self.img = PerevalImages.objects.create(img='testimage.jpg', image_name='img')  # Создаем тестовое изображение
        self.valid_payload = {
            'user': self.user.pk,
            'beauty_title': 'Test Beauty Title',
            'title': 'Test Title',
            'other_titles': 'Test Other Titles',
            'connect': 'Test Connect',
            'winter_level': 'Test Winter Level',
            'summer_level': 'Test Summer Level',
            'autumn_level': 'Test Autumn Level',
            'spring_level': 'Test Spring Level',
            'coord_id': self.coord.pk,
            'images': [self.img.pk],
            'status': 'new'
        }
        self.invalid_payload = {
            'user': '',
            'beauty_title': '',
            'title': '',
            'other_titles': '',
            'connect': '',
            'winter_level': '',
            'summer_level': '',
            'autumn_level': '',
            'spring_level': '',
            'coord_id': '',
            'images': [],
            'status': ''
        }

    def test_create_pereval_added_with_valid_payload(self):
        data = self.valid_payload
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PerevalAdded.objects.count(), 1)
        self.assertEqual(PerevalAdded.objects.get().beauty_title, 'Test Beauty Title')

    def test_create_pereval_added_with_invalid_payload(self):
        data = self.invalid_payload
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PerevalAdded.objects.count(), 0)
