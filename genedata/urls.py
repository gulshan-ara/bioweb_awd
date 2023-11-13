from django.urls import path
from . import views

urlPatterns = [
  # the request for root path serves the index function in views file
  path('', views.index, name='index'),
]