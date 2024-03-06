from django.test import TestCase
# to access Recipe model
from .models import Recipe
from .forms import RecipesSearchForm

# Create your tests here.


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name='Macaroni and Cheese',
            cooking_time=10,
            difficulty='Easy',
            ingredients='Macaroni, Cheese'
        )

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 120)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'in minutes')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        # get_absolute_url() should take you to the detail page of recipe #1
        # and load the URL /recipes/list/1
        self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

    def test_difficulty_calculation(self):
        # Access the recipe through the class attribute
        recipe = Recipe.objects.get(id=1)
        
        # Calculate the difficulty for the sample recipe
        difficulty = recipe.calculate_difficulty()
        
        # Assert that the difficulty level matches the expected result
        self.assertEqual(difficulty, 'Intermediate', "Difficulty level is not 'Intermediate'")




class RecipesSearchFormTest(TestCase):

    def test_form_renders_recipe_diff_input(self):
        form = RecipesSearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipesSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = RecipesSearchForm(
            data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipesSearchForm(data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())