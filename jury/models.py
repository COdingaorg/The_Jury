from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProject(models.Model):
  project_image = models.ImageField(upload_to = 'projects/')
  project_title = models.TextField(max_length=200)
  project_link = models.TextField()
  project_description = tinymce_models.HTMLField()
  user = models.ForeignKey(User, on_delete=CASCADE, blank=False, default=3)

  def __str__(self):
    return self.project_title

  def save_project(self):
    self.save()

  @classmethod
  def search_project(cls, search_term):
    projects = cls.objects.filter(project_title__icontains = search_term )
    return projects

  @classmethod
  def update_description(cls, id, new_desc):
    to_update = cls.objects.filter(pk = id).update(project_description = new_desc)

  @classmethod
  def delete_project(cls, id):
    to_delete = cls.objects.get(pk = id)
    to_delete.delete()
    

class UserProfile(models.Model):
  photo_path = models.ImageField(upload_to = 'user_profiles/')
  user_bio = models.TextField(max_length=200)
  facebook_account = models.TextField(max_length=100)
  twitter_account = models.TextField(max_length=100)
  instagram_account = models.TextField(max_length=100)
  user = models.ForeignKey(User, on_delete=CASCADE)
  projects = models.ForeignKey(UserProject, on_delete= CASCADE, blank=True, null=True)

  def __str__(self):
    return self.user_bio
  
  def save_user(self):
    self.save()