from django.urls import path
from .views import CashflowListView, cashflow_create, cashflow_update, cashflow_delete

urlpatterns = [
    path('', CashflowListView.as_view(), name='cashflow_list'),
    path('create/', cashflow_create, name='cashflow_create'),
    path('<int:pk>/update/', cashflow_update, name='cashflow_update'),
    path('<int:pk>/delete/', cashflow_delete, name='cashflow_delete'),
]