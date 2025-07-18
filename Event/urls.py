# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # Event URLs
    path('events/', event_list, name='event_list'),
    path('events/create/', event_create, name='event_create'),
    path('events/<int:pk>/edit/', event_update, name='event_update'),
    path('events/<int:pk>/delete/', event_delete, name='event_delete'),
    
    # Participant URLs 
    path('participants/', participant_list, name='participant_list'),
    path('participants/create/', participant_create, name='participant_create'),
    path('participants/<int:pk>/edit/', participant_update, name='participant_update'),
    path('participants/<int:pk>/delete/', participant_delete, name='participant_delete'),
    
    # Category URLs
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/edit/',category_update, name='category_update'),
    path('categories/<int:pk>/delete/',category_delete, name='category_delete'),
]