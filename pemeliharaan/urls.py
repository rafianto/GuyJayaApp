from django.urls import path
from .views import (
    PemeliharaanListView,
    PemeliharaanCreateView,
    PemeliharaanUpdateView,
    PemeliharaanDeleteView
)

app_name = 'pemeliharaan'

urlpatterns = [
    path('', PemeliharaanListView.as_view(), name='list'),
    path('create/', PemeliharaanCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', PemeliharaanUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PemeliharaanDeleteView.as_view(), name='delete'),
]