from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='item_images/', blank=False, default='logo.png')
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(blank=False, null=False)