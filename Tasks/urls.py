from django.urls import path
from .views import add_category_form, update_task_form, add_task_form
 
urlpatterns = [
    path('add-a-category/', add_category_form, name='add_task_category'),
    path('add-task/', add_task_form, name='add_task'),
    path('update-task/<int:pk>', update_task_form, name='update_task'),
]