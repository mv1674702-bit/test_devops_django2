from django.urls import path
from .views import registration, studentlist

urlpatterns = [
    path('', registration, name='registration'),
    path('studentlist/', studentlist, name='studentlist'),
]