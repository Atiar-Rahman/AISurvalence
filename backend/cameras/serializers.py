from rest_framework import serializers
from cameras.models import Camera


class CameraSerializer(serializers.ModelSerializer):

    user_email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Camera

        fields = [
            "id",
            "user_email",
            "name",
            "location",
            "camera_type",
            "source",
            "is_active",
            "ai_enabled",
            "fps",
            "resolution",
            "status",
            "snapshot",
            "last_seen",
            "created_at",
            "updated_at"
        ]

        read_only_fields = ["status","snapshot","last_seen","created_at","updated_at"]