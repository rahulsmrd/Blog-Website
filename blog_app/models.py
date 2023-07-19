from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class posts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    headding=models.CharField(max_length=100)
    upload_File=models.FileField(blank=False,null=False,upload_to='posts')
    is_it_an_Image=models.BooleanField(default=False)
    description=models.TextField(blank=True,null=True)
    published_on=models.DateTimeField(default=timezone.now)

    def Comments(self):
        return self.comments.all()

    def get_absolute_url(self):
        return reverse('blog_app:post_list')


class comment(models.Model):
    user_comments=models.ForeignKey(posts,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=150)
    text=models.CharField(max_length=1000)
    published_date=models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog_app:post_list')
    