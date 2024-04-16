
from django.urls import path
from . import views

#generate a urls for my views
urlpatterns = [
    path('', views.index, name='index'),]