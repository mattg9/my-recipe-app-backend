# recipes/views.py
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from django.http import JsonResponse

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

def search_recipes(request):
    query = request.GET.get('query')
    results = Recipe.objects.filter(name__icontains=query)
    serialized_results = [recipe.serialize() for recipe in results]
    return JsonResponse(serialized_results, safe=False)
