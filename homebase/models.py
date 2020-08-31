from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class WinescipeUser(AbstractUser):
    profile_image = ProcessedImageField(
        upload_to = 'static/images/profile',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
        )
        
        
class ImagePost(models.Model):
    author = models.ForeignKey(WinescipeUser,on_delete=models.CASCADE,related_name='my_posts')
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
    
class Like(models.Model):
    post = models.ForeignKey(ImagePost,on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(WinescipeUser,on_delete=models.CASCADE,related_name='likes')
    class Meta:
        unique_together = ("post", "user")
    def __str__(self):
        return self.user.username + ' likes ' + self.post.title
        
class Comment(models.Model):
    post = models.ForeignKey(ImagePost,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(WinescipeUser,on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    posted_on = models.DateTimeField(auto_now_add=True,editable=False)
    def __str__(self):
        return self.user.username + ' add a comment to Post:  ' + self.post.title
    
