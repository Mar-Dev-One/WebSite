from django.test import TestCase
from .models import YourModel  # Replace with your actual model
from rest_framework import status
from rest_framework.test import APIClient

class YourModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.model_instance = YourModel.objects.create(field1='value1', field2='value2')  # Replace with actual fields

    def test_model_creation(self):
        response = self.client.post('/api/yourmodel/', {'field1': 'value1', 'field2': 'value2'}, format='json')  # Adjust URL and data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_model_retrieval(self):
        response = self.client.get(f'/api/yourmodel/{self.model_instance.id}/', format='json')  # Adjust URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['field1'], self.model_instance.field1)

    def test_model_update(self):
        response = self.client.put(f'/api/yourmodel/{self.model_instance.id}/', {'field1': 'new_value'}, format='json')  # Adjust URL and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.model_instance.refresh_from_db()
        self.assertEqual(self.model_instance.field1, 'new_value')

    def test_model_deletion(self):
        response = self.client.delete(f'/api/yourmodel/{self.model_instance.id}/', format='json')  # Adjust URL
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(YourModel.objects.filter(id=self.model_instance.id).exists())