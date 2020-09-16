from django.conf.urls import url
from todoapp import views as todo_view


app_name = 'todoapp'

urlpatterns = [
    url(r'^$',todo_view.TaskListView.as_view(),name='task_list'),
    url(r'^create/',todo_view.TaskCreateView.as_view(),name='task_create'),
    
    
]
