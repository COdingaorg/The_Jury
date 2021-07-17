from django.conf.urls import url
from jury import views

urlpatterns = {
  url(r'^$', views.index, name = 'home'),
}