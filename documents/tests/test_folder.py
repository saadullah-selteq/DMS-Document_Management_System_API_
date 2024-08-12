# documents/tests/test_folder.py

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from documents.tests.factories import BusinessFactory, FolderFactory


@pytest.mark.django_db
def test_create_business_folder():
    client = APIClient()
    business = BusinessFactory.create()
    url = reverse('folder-create_business_folder')
    data = {'business_id': business.id, 'name': 'Test Folder'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Test Folder'
    assert response.data['business'] == business.id


@pytest.mark.django_db
def test_create_sub_business_folder():
    client = APIClient()
    sub_business = BusinessFactory.create()
    url = reverse('folder-create_sub_business_folder')
    data = {'sub_business_id': sub_business.id, 'name': 'Test Sub Folder' }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Test Sub Folder'
    assert response.data['sub_business'] == sub_business.id


@pytest.mark.django_db
def test_get_file_folder():
    client = APIClient()
    folder = FolderFactory.create()
    url = reverse('folder-get_file_folder', args=[folder.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == folder.name
    assert response.data['id'] == folder.id
