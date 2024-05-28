# recipes/urls.py
from django.urls import path
from .views import RecipeListCreateView, search_recipes

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('search/', search_recipes, name='recipe-search'),
]
