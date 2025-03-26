from django.urls import path
from . import views  # Make sure this import is correct

app_name = 'kolam'  # Add this in your kolam/urls.py

urlpatterns = [
    path('', views.KolamListView.as_view(), name='list'),
    path('create/', views.kolam_create, name='create'),
    path('<int:pk>/edit/', views.kolam_update, name='update'),
    path('<int:pk>/delete/', views.kolam_delete, name='delete'),
]