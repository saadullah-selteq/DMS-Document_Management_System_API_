# documents/tests/test_views.py

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from documents.models import Business, SubBusiness, Folder, File
from documents.tests.factories import BusinessFactory, FolderFactory, FileFactory

@pytest.mark.django_db
def test_business_list_view():
    client = APIClient()
    BusinessFactory.create_batch(3)
    response = client.get(reverse('business-list'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

@pytest.mark.django_db
def test_sub_business_list_view():
    client = APIClient()
    business = BusinessFactory.create()
    SubBusiness.objects.create(name='Test Sub Business', parent=business)
    response = client.get(reverse('subbusiness-list'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_create_folder_view():
    client = APIClient()
    business = BusinessFactory.create()
    url = reverse('folder-create_business_folder')
    data = {'business_id': business.id, 'name': 'Test Folder'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Test Folder'
    assert response.data['business'] == business.id

@pytest.mark.django_db
def test_upload_file_view():
    client = APIClient()
    folder = FolderFactory.create()
    url = reverse('file-upload_file')
    file_content = b'Test file content'
    response = client.post(url, {'folder_id': folder.id, 'file': file_content}, format='multipart')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['folder'] == folder.id

@pytest.mark.django_db
def test_folder_detail_view():
    client = APIClient()
    folder = FolderFactory.create()
    url = reverse('folder-detail', args=[folder.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == folder.id
    assert response.data['name'] == folder.name
