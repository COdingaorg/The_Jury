from django.shortcuts import render

# Create your views here.
def index(request):
  title = 'The Jury-Home'

  context = {
    'title':title
  }
  return render(request, 'app_templates/index.html', context)
