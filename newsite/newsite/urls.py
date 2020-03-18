from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^$', views.homepage),
]



#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

