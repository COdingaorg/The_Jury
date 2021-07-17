from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import registerUser
from .models import User
from django.contrib.auth import authenticate, login

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
