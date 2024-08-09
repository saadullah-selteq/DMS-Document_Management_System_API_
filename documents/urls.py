from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet, SubBusinessViewSet, FolderViewSet, FileViewSet

router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'sub-businesses', SubBusinessViewSet)
router.register(r'folders', FolderViewSet)
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
