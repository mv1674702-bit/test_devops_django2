from django.urls import path
from application.views import home, taskDisplay, taskUpdate, taskDelete

urlpatterns = [
    path('', home, name='home'),
    path('task', taskDisplay, name='task'),
    path('taskupdate/<int:id>', taskUpdate, name = 'taskup'),
    path('del/<int:id>', taskDelete, name = 'delete')
]