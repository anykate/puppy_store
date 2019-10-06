from django.urls import path
from . import views


app_name = 'puppies'

urlpatterns = [
    path('api/v1/puppies/<int:puppy_id>/', views.get_delete_update_puppy,
         name='get_delete_update_puppy'),
    path('api/v1/puppies/', views.get_post_puppies, name='get_post_puppies'),
]
