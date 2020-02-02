from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('finish/<list_id>', views.finish, name='finish'),
    path('unfinish/<list_id>', views.unfinish, name='unfinish'),
    path('edit/<list_id>', views.edit, name='edit'),
]
    