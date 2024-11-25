from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photo-upload', views.photo_upload, name='photo_upload'),
    path('update-photo/<int:p_id>', views.update_photo, name='update_photo'),
    path('delete-photo/<int:p_id>', views.delete_photo, name='delete_photo'),
]
