# documents/tests/test_models.py

import pytest
from documents.models import Business, SubBusiness, Folder, File

@pytest.mark.django_db
def test_business_model():
    business = Business.objects.create(name='Test Business', Description='Test Description')
    assert business.name == 'Test Business'
    assert business.Description == 'Test Description'

@pytest.mark.django_db
def test_sub_business_model():
    business = Business.objects.create(name='Parent Business', Description='Parent Description')
    sub_business = SubBusiness.objects.create(name='Test Sub Business', parent=business)
    assert sub_business.name == 'Test Sub Business'
    assert sub_business.parent == business

@pytest.mark.django_db
def test_folder_model():
    business = Business.objects.create(name='Test Business', Description='Test Description')
    folder = Folder.objects.create(name='Test Folder', business=business)
    assert folder.name == 'Test Folder'
    assert folder.business == business

@pytest.mark.django_db
def test_file_model():
    business = Business.objects.create(name='Test Business', Description='Test Description')
    folder = Folder.objects.create(name='Test Folder', business=business)
    file = File.objects.create(name='Test File', folder=folder)
    assert file.name == 'Test File'
    assert file.folder == folder
