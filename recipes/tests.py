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
    
    def test_get_recipes(self):
        recipe_count = Recipe.objects.count()
        response = self.client.get('/api/recipes/')
        self.assertEqual(response.status_code , 200)
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], recipe_count)
        self.assertEqual(len(response.data['results']), recipe_count)

    def test_update_recipe(self):
        recipe = Recipe.objects.first()
        recipe_attrs = {
            'title' : 'New Recipe Name',
            'ingredients' : 'My\nNew\nList\nOf\nIngredients',
            'instructions' :'My\nNew\nInstructions'
        }
        response = self.client.patch(f"/api/recipes/{recipe.id}/", recipe_attrs, format='json')
        self.assertEqual(response.status_code , 200)
        updated = Recipe.objects.get(id=recipe.id)
        for attr, expected_value in recipe_attrs.items():
            self.assertEqual(getattr(updated, attr), expected_value)
