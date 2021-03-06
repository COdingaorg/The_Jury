from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce import models as tinymce_models
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProject(models.Model):
  project_image = models.ImageField(upload_to = 'projects/')
  project_title = models.CharField(max_length=200)
  project_link = models.CharField(max_length=100)
  created_on = models.DateField(default='2021-07-18')
  project_description = tinymce_models.HTMLField()
  user = models.ForeignKey(User, on_delete=CASCADE, blank=False, default=3)
  class Meta:
    ordering = ['-id']

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
  facebook_account = models.CharField(max_length=50)
  twitter_account = models.CharField(max_length=50)
  instagram_account = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=CASCADE)
  projects = models.ForeignKey(UserProject, on_delete= CASCADE, blank=True, null=True)

  class Meta:
    ordering = ['-id']

  def __str__(self):
    return self.user_bio
  
  def save_profile(self):
    self.save()

  @classmethod
  def get_user_profile(cls, usernm):
    user_id = (User.objects.get(username = usernm)).id
    user_profile = cls.objects.filter(user = user_id).first()
    return user_profile

  @classmethod
  def update_bio(cls, id, new_bio):
    to_update = UserProfile.objects.filter(pk =id)
    to_update.update(user_bio = new_bio)

  @classmethod
  def delete_profile(cls,id):
    to_delete =cls.objects.get(pk = id)
    to_delete.delete()

class ApplicationRating(models.Model):
  design_rate = models.IntegerField(default=1, validators=[MaxValueValidator(10, 'Must be less than or equal 10'),MinValueValidator(1, 'cannot be less than 1')])
  usability_rate = models.IntegerField(default=1, validators=[MaxValueValidator(10, 'Must be less than or equal 10'),MinValueValidator(1, 'cannot be less than 1')])
  content_rate = models.IntegerField(default=1, validators=[MaxValueValidator(10, 'Must be less than or equal 10'),MinValueValidator(1, 'cannot be less than 1')])
  score_description = models.TextField(blank=True)
  user_profile = models.ForeignKey(UserProfile, on_delete=CASCADE, default=3)
  project = models.ForeignKey(UserProject, on_delete=CASCADE)


