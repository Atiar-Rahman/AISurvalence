from rest_framework import serializers
from alert.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    camera_name = serializers.ReadOnlyField(source='camera.name')
    class Meta:
        model = Notification
        fields = ['id','user','camera','camera_name','alert_type','message','is_read','created_at']

    