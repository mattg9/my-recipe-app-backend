# recipes/views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

@api_view(['GET'])
def search_recipes(request):
    query = request.GET.get('query', '')
    if not query:
        return Response({"detail": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST)
    results = Recipe.objects.filter(title__icontains=query)
    serialized_results = RecipeSerializer(results, many=True).data
    return Response(serialized_results)
