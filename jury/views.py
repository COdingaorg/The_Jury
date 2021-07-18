from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import registerUser, UploadProjectForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  title = 'The Jury-Home'

  context = {
    'title':title
  }
  return render(request, 'app_templates/index.html', context)

def register_user(request):
  form = registerUser
  title = 'Register-The Jury'
  if request.method == 'POST':
    form = registerUser(request.POST)
    if form.is_valid():
      uname = form.cleaned_data['username']
      password = form.cleaned_data['password2']
      form.save()
      
      to_login = authenticate(username = uname , password = password )
      login(request, to_login)

      messages.success(request, 'Account Created Successfully!. Check out our Email later :)')
      return redirect('/')
    else:
      messages.warning(request, 'invalid input')
  else:
    form = registerUser
  context = {
    'title':title,
    'form':form,
  }
  return render(request, 'django_registration/registration_form.html', context)

#A form to submit a users project for rating and reviews
@login_required(login_url = 'login')
def upload_project(request):
  form = UploadProjectForm
  title = 'Submit Project - The Jury'

  context = {
    'title': title,
    'form': form,
  }
  return render(request, 'app_templates/upload_project.html', context)
