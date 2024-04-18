from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo_item, name='add_todo_item'),
    path('toggle/<int:item_id>/', views.toggle_todo_item, name='toggle_todo_item'),
    path('calendar/', views.calendar_view, name='calendar_view'),
]
