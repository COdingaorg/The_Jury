from django.conf.urls import url
from jury import views

urlpatterns = [
  url(r'^$', views.index, name = 'home'),
  url(r'^register_user/$', views.register_user, name = 'register_user')
]