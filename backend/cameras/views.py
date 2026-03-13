from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cameras.serializers import CameraSerializer
from cameras.models import Camera
from rest_framework import permissions
# Create your views here.

class CameraViewSet(ModelViewSet):
    """
    this is camera viewset. this viewset use to crud operation in Camera model
    
    """
    serializer_class = CameraSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Camera.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
