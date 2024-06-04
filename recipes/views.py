from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

class RecipePagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class RecipeCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = RecipePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['ingredients', 'instructions']

class RecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    lookup_field = 'id'
    serializer_class = RecipeSerializer

    def delete(self, request, *args, **kwargs):
        recipe_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if (response.status_code == 204):
            from django.core.cache import cache
            cache.delete(f"recipe_data_${recipe_id}")
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if (response.status_code == 200):
            from django.core.cache import cache
            recipe = response.data
            cache.set(f"recipe_data_${recipe['id']}", {
                'title' : recipe['title'],
                'description' : recipe['description']
            })
        return response
