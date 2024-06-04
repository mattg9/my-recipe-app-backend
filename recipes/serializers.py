from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(default=None)
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'prep_time', 'cook_time',
                  'servings', 'photo']
