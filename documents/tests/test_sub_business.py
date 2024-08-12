# documents/tests/test_sub_business.py

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from documents.tests.factories import BusinessFactory

@pytest.mark.django_db
def test_create_sub_business():
    client = APIClient()
    business = BusinessFactory.create()
    url = reverse('subbusiness-list')
    data = {'name': 'Test Sub Business', 'parent': business.id}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Test Sub Business'
    assert response.data['parent'] == business.id
