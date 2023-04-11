from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PerevalAdded


class PerevalAddedTests(APITestCase):
    def setUp(self):
        self.url = reverse('submit_data')
        self.valid_payload = {
            'user': 1,
            'beauty_title': 'Test Beauty Title',
            'title': 'Test Title',
            'other_titles': 'Test Other Titles',
            'connect': 'Test Connect',
            'winter_level': 'Test Winter Level',
            'summer_level': 'Test Summer Level',
            'autumn_level': 'Test Autumn Level',
            'spring_level': 'Test Spring Level',
            'coord_id': 1,
            'images': [1, 2],
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
    print(PerevalAdded.objects.get().beauty_title)
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
