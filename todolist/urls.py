from django.urls import path
from todolist.views import show_todolist_lobby, show_task, login_user, logout_user, register_user, new_task, todolist_json, new_task_instant

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_lobby, name='lobby'),
    path('task/', show_task, name='task'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('new_task/', new_task, name='new_task'),
    path('json/', todolist_json, name='json'),
    path('add/', new_task_instant, name='new_instant'),
]