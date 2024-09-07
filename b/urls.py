from django.urls import path , include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





urlpatterns = [
    path("",views.homepage , name='homepage'),
    ]
urlpatterns += staticfiles_urlpatterns()
