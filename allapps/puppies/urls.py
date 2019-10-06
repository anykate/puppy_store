from django.urls import path
from . import views


app_name = 'puppies'

urlpatterns = [
    path('', views.index, name='index'),
]
