from rest_framework.test import APITestCase
from .models import Recipe

class RecipeCreateTestCases(APITestCase):

    fixtures = ['recipes.json']

    def test_create_recipe(self):
        recipe_count = Recipe.objects.count()
        recipe_attrs = {
            'title': 'Beef Stew',
            'ingredients': 'Beef\nCarrots\nPotatoes\nStock',
            'instructions': 'Preheat slow cooker\nPut everything in the pot\nCook for 30 minutes',
            'prep_time': '00:05:00',
            'cook_time': '00:30:00'
        }
        response = self.client.post('/api/recipes/', recipe_attrs)
        if (response.status_code != 201):
            print(response.status_code)
            print(response.data)
        self.assertEqual(
            Recipe.objects.count(),
            recipe_count + 1,
        )
        for attr, expected_value in recipe_attrs.items():
            self.assertEqual(response.data[attr], expected_value)
        self.assertEqual(response.data['servings'], 1)

    def test_delete_recipe(self):
        recipe_count = Recipe.objects.count()
        recipe_id = Recipe.objects.first().id
        response = self.client.delete(f"/api/recipes/{recipe_id}/")
        if (response.status_code != 204):
            print(response.status_code)
        self.assertEqual(
            Recipe.objects.count(),
            recipe_count - 1
        )
        self.assertRaises(
            Recipe.DoesNotExist,
            Recipe.objects.get, id=recipe_id
        )
    