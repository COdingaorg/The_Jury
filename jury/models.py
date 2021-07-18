from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProfile(models.Model):
  photo_path = models.ImageField(upload_to = 'projects/')
  user_bio = models.TextField(max_length=200)
  facebook_account = models.TextField(max_length=100)
  twitter_account = models.TextField(max_length=100)
  instagram_account = models.TextField(max_length=100)
  user = models.ForeignKey(User, on_delete=CASCADE)
  
