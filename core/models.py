from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='item_images/', blank=False, default='logo.png')
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name

class Request(models.Model):
    title = models.CharField(blank=True, max_length=255)
    phone_number = models.IntegerField(blank=True)
    userinfo = models.TextField(blank=True)
    item = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.title