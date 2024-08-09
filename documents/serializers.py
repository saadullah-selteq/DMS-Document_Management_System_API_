from rest_framework import serializers
from .models import Business, SubBusiness, Folder, File

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class SubBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubBusiness
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
