from django.urls import path
from .views import RecipeCreateView, RecipeRetrieveUpdateDestroy

urlpatterns = [
    path('recipes/', RecipeCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroy.as_view(), name='recipe-retrieve-update-destroy'),
]
