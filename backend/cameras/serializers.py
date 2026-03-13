
from cameras.models import Camera
from rest_framework.serializers import ModelSerializer

class CameraSerializer(ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id','name','location','camera_type','source','is_active','ai_enabled','fps','resolution','last_seen','created_at','updated_at']  
