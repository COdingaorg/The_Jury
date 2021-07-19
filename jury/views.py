from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import registerUser, UploadProjectForm,AddorEditProfile
from .models import User, UserProfile, UserProject
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime as dt

# Create your views here.
def index(request):
  '''
  Renders user profile
  Renders projects
  Renders project of the day
  '''
  title = 'The Jury-Home'
  try:
    user_profile = UserProfile.objects.filter(user = request.user.id).first()
  except UserProfile.DoesNotExist:
    user_profile = None

  try:
    user_projects = UserProject.objects.all()
  except UserProfile.DoesNotExist:
    user_projects = None

  try:
    proj_day = UserProject.objects.all().first()
  except:
    proj_day = UserProject.objects.get(pk = 4)

  date_today= dt.date.today()

  context = {
    'date_today':date_today,
    'proj_day':proj_day,
    'user_projects':user_projects,
    'user_profile':user_profile,
    'title':title,
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
  '''
  A view function rendering to upload form template.
  '''
  form = UploadProjectForm
  title = 'Submit Project - The Jury'
  if request.method == 'POST':
    form = UploadProjectForm(request.POST, request.FILES)
    if form.is_valid():
      new_project_item = form.save(commit=False)
      new_project_item.user = request.user

      new_project_item.save()

      messages.success(request, 'Post Added Successfully!')
      
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
      raise ValueError('Invalid data Entered')
  else:
    context = {
      'title': title,
      'form': form,
    }
    return render(request, 'app_templates/upload_project.html', context)

#A search user view function
def get_project(request):
  '''
  A view fuction responsible for returning searched user
  '''
  try:
    user_profile = UserProfile.objects.filter(user = request.user.id).first()
  except UserProfile.DoesNotExist:
    user_profile = None

  if 'search_term' in request.GET and request.GET['search_term']:
    search_trm = request.GET.get('search_term')
    projects = UserProject.objects.filter(project_title__icontains = search_trm)

    try:
      user_profile = UserProfile.objects.filter(user = request.user.id).first()
    except UserProfile.DoesNotExist:
      user_profile = None

    context = {
      'user_profile':user_profile,
      'projects':projects,
      'search_trm':search_trm
    }

    return render(request, 'app_templates/search_result.html', context)
  
  else:
    title = 'Search Projects'
    message = 'No Projects Found'
    context = {
      'user_profile':user_profile,
      'message':message,
      'title':title
    }
    
    return render(request, 'app_templates/search_result.html', context)

#A view function rendering to profile
@login_required(login_url='login')
def user_profile(request):
  '''
  View function that displays to profile page
  result 1- Adds to profile if none
  result 2- Edits profile
  '''
  title = f'{request.user.username}\'s Profile'
  form = AddorEditProfile
  if request.method == 'POST':
    form = AddorEditProfile(request.POST, request.FILES)
    if form.is_valid():
      new_profile = form.save(commit=False)
      new_profile.user = request.user

      new_profile.save()
      try:
        user_profile = UserProfile.objects.filter(user = request.user.id).first()
      except UserProfile.DoesNotExist:
        user_profile = None

      context = {
        'title' :title,
        'form':form,
        'user_profile':user_profile,
        }

      return render(request,'app_templates/profile.html', context )

  else:
    try:
      user_profile = UserProfile.objects.filter(user = request.user.id).first()
    except UserProfile.DoesNotExist:
        user_profile = None

    try:
      user_projects = UserProject.objects.filter(user = request.user.id)
    except UserProject.DoesNotExist:
      user_projects = None

        
    context = {
      'user_posts':user_projects,
      'title' :title,
      'form':form,
      'user_profile':user_profile,
      }
    
    return render(request, 'app_templates/profile.html', context)