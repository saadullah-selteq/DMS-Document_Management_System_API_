
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .factories import  BusinessFactory
@pytest.mark.django_db
def test_create_business_api():
    client = APIClient()
    url = reverse('business-list')
    data = {'name': 'New Business', 'Description': 'A new business description'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'New Business'


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
