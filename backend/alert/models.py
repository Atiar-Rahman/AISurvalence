from django.db import models
from users.models import User
from cameras.models import Camera

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='notifications'
    )
    camera = models.ForeignKey(
        Camera,
        on_delete = models.CASCADE,
        related_name='notifications'
    )

    alert_type = models.CharField(max_length=50)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.camera.name} - {self.alert_type}'
    
