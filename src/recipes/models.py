from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    difficulty = models.CharField(max_length=50, default='unknown')
    ingredients = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 7:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) <= 2:
            difficulty = 'Easy'  # Assign 'Easy' for cooking time 10 and ingredient count 2
        elif self.cooking_time >= 10 and len(ingredients) <= 7:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Hard'
        return difficulty