from django.urls import path
from . import views

urlpatterns = [
  # the request for root path serves the index function in views file
  path('', views.index, name='index'),
]