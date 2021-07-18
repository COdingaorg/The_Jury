from jury.models import UserProfile, UserProject
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerUser(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UploadProjectForm(forms.ModelForm):
  class Meta:
    model = UserProject
    fields = ['project_title', 'project_image', 'project_description', 'project_link']

class AddorEditProfile(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ['photo_path', 'user_bio', 'facebook_account', 'twitter_account', 'instagram_account']
