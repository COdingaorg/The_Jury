from django.conf.urls import url
from jury import views

urlpatterns = [
  url(r'^$', views.index, name = 'home'),
  url(r'^register_user/$', views.register_user, name = 'register_user'),
  url(r'^upload_project/$', views.upload_project, name = 'upload_project'),
  url(r'^search_user/$', views.get_user, name= 'get_user'),
  url(r'^profile_page/$', views.user_profile, name = 'user_profile'),
]