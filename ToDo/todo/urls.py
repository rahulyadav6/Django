from django.urls import path
from . import views
urlpatterns = [
    # Add task
    path('addTasks/', views.addTask, name='addTask'),
    # Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as undoe
    path('mark_as_unDone/<int:pk>/', views.mark_as_unDone, name='mark_as_unDone'),
    # Edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
