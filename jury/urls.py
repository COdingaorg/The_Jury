from django.conf.urls import url
from django.conf.urls.static import static
from jury import views
from django.conf import settings

urlpatterns = [
  url(r'^$', views.index, name = 'home'),
  url(r'^register_user/$', views.register_user, name = 'register_user'),
  url(r'^upload_project/$', views.upload_project, name = 'upload_project'),
  url(r'^search_user/$', views.get_project, name= 'get_project'),
  url(r'^profile_page/$', views.user_profile, name = 'user_profile'),
  url(r'^project/(\d+)/$', views.single_project, name = 'single_project'),
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)