# documents/tests/test_business.py

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_create_business():
    client = APIClient()
    url = reverse('business-list')
    data = {'name': 'Test Business', 'Description': 'Test Description'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Test Business'
    assert response.data['Description'] == 'Test Description'
