from django.test import TestCase
# to access Recipe model
from .models import Recipe

# Create your tests here.


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name='Macaroni and Cheese',
            cooking_time='10',
            difficulty='Easy',
            ingredients='Macaroni, Cheese'
    )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertEqual(cooking_time, 10)

    def test_ingredients_list(self):
        recipe = Recipe.objects.get(id=1)
        ingredients = recipe.ingredients
        self.assertEqual(ingredients, 'Macaroni, Cheese')

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        print("Cooking Time:", recipe.cooking_time)
        print("Ingredients Length:", len(recipe.ingredients.split(', ')))
        print(recipe.calculate_difficulty())
        self.assertEqual(recipe.calculate_difficulty(), 'Easy')