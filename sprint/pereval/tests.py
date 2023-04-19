from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PerevalAdded, Users, Coords, PerevalImages


class PerevalAddedTests(APITestCase):
    def setUp(self):
        self.url_post = reverse('submit_data')
        self.url_get = reverse('get_data', kwargs={'pk': 2})
        self.user = Users.objects.create(first_name='TestUser', last_name='TestUser', password='testpassword',
                                         email='TestEmail', otc='TestUser')
        self.coord = Coords.objects.create(latitude=1.0, longitude=2.0, height=2.0)
        self.img = PerevalImages.objects.create(img='testimage.jpg', image_name='testimage')
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
        self.valid_update = {
            "user": self.user.id,
            "beauty_title": "Updated beauty title",
            "title": "Updated title",
            "other_titles": "Updated other titles",
            "connect": "Updated connect",
            "winter_level": "Updated winter level",
            "summer_level": "Updated summer level",
            "autumn_level": "Updated autumn level",
            "spring_level": "Updated spring level",
            "coord_id": self.coord.id,
            "status": "new"
        }

    def test_create_pereval_added_with_valid_payload(self):
        data = self.valid_payload
        response = self.client.post(self.url_post, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PerevalAdded.objects.count(), 1)
        self.assertEqual(PerevalAdded.objects.get().beauty_title, 'Test Beauty Title')

    def test_create_pereval_added_with_invalid_payload(self):
        data = self.invalid_payload
        response = self.client.post(self.url_post, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PerevalAdded.objects.count(), 0)

    def test_get_existing_pereval(self):
        user = self.user
        coord = self.coord
        pereval = PerevalAdded.objects.create(user=user,
                                              beauty_title='Test Beauty Title',
                                              title='Test Title',
                                              other_titles='Test Other Titles',
                                              connect='Test Connect',
                                              winter_level='Test Winter Level',
                                              summer_level='Test Summer Level',
                                              autumn_level='Test Autumn Level',
                                              spring_level='Test Spring Level',
                                              coord_id=coord,
                                              status='new')
        url = reverse('get_data', args=[pereval.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PerevalAdded.objects.get().beauty_title, 'Test Beauty Title')

    def test_get_not_existing_pereval(self):
        response = self.client.get(self.url_get)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_edit_pereval_added_with_valid_update(self):
        pereval = PerevalAdded.objects.create(user=self.user,
                                              beauty_title='Test Beauty Title',
                                              title='Test Title',
                                              other_titles='Test Other Titles',
                                              connect='Test Connect',
                                              winter_level='Test Winter Level',
                                              summer_level='Test Summer Level',
                                              autumn_level='Test Autumn Level',
                                              spring_level='Test Spring Level',
                                              coord_id=self.coord,
                                              status='new')
        url = reverse('update_data', args=[pereval.pk])
        response = self.client.patch(url, self.valid_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['state'], 1)
        self.assertEqual(PerevalAdded.objects.get().beauty_title,
                         self.valid_update['beauty_title'])

    def test_edit_pereval_added_with_invalid_update(self):
        pereval = PerevalAdded.objects.create(user=self.user,
                                              beauty_title='Test Beauty Title',
                                              title='Test Title',
                                              other_titles='Test Other Titles',
                                              connect='Test Connect',
                                              winter_level='Test Winter Level',
                                              summer_level='Test Summer Level',
                                              autumn_level='Test Autumn Level',
                                              spring_level='Test Spring Level',
                                              coord_id=self.coord,
                                              status='accepted')
        url = reverse('update_data', args=[pereval.pk])
        response = self.client.patch(url, self.valid_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['state'], 0)
        self.assertEqual(response.data['message'], 'Pereval status is not "new"')
