from django.urls import path
from . import views

urlpatterns = [
    path('states/', views.state_list, name='state_list'),
    path('states/create/', views.create_state, name='create_state'),
    path('states/update/<int:pk>/', views.update_state, name='update_state'),
    path('states/delete/<int:pk>/', views.delete_state, name='delete_state'),
    path('places/create/', views.create_place, name='create_place'),
    path('places/update/<int:pk>/', views.update_place, name='update_place'),
    path('places/delete/<int:pk>/', views.delete_place, name='delete_place'),
]
