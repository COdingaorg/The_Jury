from jury.models import UserProject
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
