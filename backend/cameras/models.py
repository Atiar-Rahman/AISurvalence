from django.db import models
from users.models import User
# Create your models here.

class Camera(models.Model):

    CAMERA_TYPE = (
        ("webcam","Webcam"),
        ("rtsp","RTSP"),
    )
    STATUS = (
        ("online","Online"),
        ("offline","Offline"),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="cameras")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    camera_type = models.CharField(max_length=10,choices=CAMERA_TYPE)
    source = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    ai_enabled = models.BooleanField(default=True)
    fps = models.IntegerField(default=30)
    resolution = models.CharField(max_length=20, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS,default="offline")
    snapshot = models.ImageField(upload_to="snapshots/", blank=True, null=True)
    
    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return self.name
