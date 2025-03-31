from django.urls import path # type: ignore
from . import views  # Make sure this import is correct

app_name = 'kolam'  # Add this in your kolam/urls.py

urlpatterns = [
    path('', views.KolamListView.as_view(), name='kolam_list'),
    path('create/', views.kolam_create, name='kolam_create'),
    path('<int:pk>/edit/', views.kolam_update, name='kolam_update'),
    path('<int:pk>/delete/', views.kolam_delete, name='kolam_delete'),
]