from django.shortcuts import render
from .forms import registerUser

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

  context = {
    'title':title,
    'form':form,
  }  
  return render(request, 'django_registration/registration_form.html', context)
