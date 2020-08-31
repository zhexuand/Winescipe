from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ImagePost(models.Model):
    title = models.TextField(blank = True,null = True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
        )
    def get_absolute_url(self):
        return reverse("postdetail",args=[str(self.id)])

class WinescipeUser(AbstractUser):
    profile_image = ProcessedImageField(
        upload_to = 'static/images/profile',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
        )
    
