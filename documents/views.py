from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Business, SubBusiness, Folder, File
from .serializers import BusinessSerializer, SubBusinessSerializer, FolderSerializer, FileSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class SubBusinessViewSet(viewsets.ModelViewSet):
    queryset = SubBusiness.objects.all()
    serializer_class = SubBusinessSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    @action(detail=False, methods=['post'])
    def create_business_folder(self, request):
        business_id = request.data.get('business_id')
        name = request.data.get('name')
        parent_folder_id = request.data.get('parent_folder_id')

        if not business_id or not name:
            return Response({'error': 'Business ID and name are required.'}, status=status.HTTP_400_BAD_REQUEST)

        business = Business.objects.get(id=business_id)
        parent_folder = Folder.objects.get(id=parent_folder_id) if parent_folder_id else None

        new_folder = Folder.objects.create(name=name, business=business, parent_folder=parent_folder)
        serializer = self.get_serializer(new_folder)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def create_sub_business_folder(self, request):
        sub_business_id = request.data.get('sub_business_id')
        name = request.data.get('name')
        parent_folder_id = request.data.get('parent_folder_id')

        if not sub_business_id or not name:
            return Response({'error': 'Sub Business ID and name are required.'}, status=status.HTTP_400_BAD_REQUEST)

        sub_business = SubBusiness.objects.get(id=sub_business_id)
        parent_folder = Folder.objects.get(id=parent_folder_id) if parent_folder_id else None

        new_folder = Folder.objects.create(name=name, sub_business=sub_business, parent_folder=parent_folder)
        serializer = self.get_serializer(new_folder)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def get_file_folder(self, request, pk=None):
        folder = Folder.objects.get(pk=pk)
        serializer = self.get_serializer(folder)
        return Response(serializer.data)


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['post'])
    def upload_file(self, request):
        folder_id = request.data.get('folder_id')
        file = request.FILES.get('file')

        if not folder_id or not file:
            return Response({'error': 'Folder ID and file are required.'}, status=status.HTTP_400_BAD_REQUEST)

        folder = Folder.objects.get(id=folder_id)
        new_file = File.objects.create(name=file.name, folder=folder, file=file)
        serializer = self.get_serializer(new_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
#serializers,