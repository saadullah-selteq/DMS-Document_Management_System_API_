# documents/tests/test_serializers.py

from documents.models import Business, SubBusiness, Folder, File
from documents.serializers import BusinessSerializer, SubBusinessSerializer, FolderSerializer, FileSerializer


def test_business_serializer():
    data = {'name': 'Test Business', 'Description': 'Test Description'}
    serializer = BusinessSerializer(data=data)
    assert serializer.is_valid()
    business = serializer.save()
    assert business.name == 'Test Business'
    assert business.Description == 'Test Description'


def test_sub_business_serializer():
    business = Business.objects.create(name='Parent Business', Description='Parent Description')
    data = {'name': 'Test Sub Business', 'parent': business.id}
    serializer = SubBusinessSerializer(data=data)
    assert serializer.is_valid()
    sub_business = serializer.save()
    assert sub_business.name == 'Test Sub Business'
    assert sub_business.parent == business


def test_folder_serializer():
    business = Business.objects.create(name='Test Business', Description='Test Description')
    data = {'name': 'Test Folder', 'business': business.id}
    serializer = FolderSerializer(data=data)
    assert serializer.is_valid()
    folder = serializer.save()
    assert folder.name == 'Test Folder'
    assert folder.business == business


def test_file_serializer():
    business = Business.objects.create(name='Test Business', Description='Test Description')
    folder = Folder.objects.create(name='Test Folder', business=business)
    data = {'name': 'Test File', 'folder': folder.id}
    serializer = FileSerializer(data=data)
    assert serializer.is_valid()
    file = serializer.save()
    assert file.name == 'Test File'
    assert file.folder == folder
