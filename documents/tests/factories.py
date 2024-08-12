# documents/tests/factories.py

import factory
from factory.django import DjangoModelFactory
from documents.models import Business, SubBusiness, Folder, File


class BusinessFactory(DjangoModelFactory):
    class Meta:
        model = Business

    name = factory.Faker('company')
    Description = factory.Faker('catch_phrase')


class SubBusinessFactory(DjangoModelFactory):
    class Meta:
        model = SubBusiness

    name = factory.Faker('company')
    parent = factory.SubFactory(BusinessFactory)


class FolderFactory(DjangoModelFactory):
    class Meta:
        model = Folder

    name = factory.Faker('word')
    business = factory.SubFactory(BusinessFactory)


class FileFactory(DjangoModelFactory):
    class Meta:
        model = File

    name = factory.Faker('file_name')
    folder = factory.SubFactory(FolderFactory)
    file = factory.django.FileField(filename='test_file.txt')
