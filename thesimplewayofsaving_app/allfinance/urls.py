from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('create-budget/', views.create_budget, name='create_budget'),
    path('list-budgets/', views.list_budgets, name='list_budgets'),
    path('login/', views.user_login, name='login'),  # URL para a visualização de login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para a visualização de logout
]