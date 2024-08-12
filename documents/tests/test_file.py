# documents/tests/test_file.py

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from documents.tests.factories import FolderFactory

@pytest.mark.django_db
def test_upload_file():
    client = APIClient()
    folder = FolderFactory.create()
    url = reverse('file-upload_file')
    file_content = b'Test file content'
    response = client.post(
        url,
        {'folder_id': folder.id, 'file': file_content},
        format='multipart'
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['folder'] == folder.id
