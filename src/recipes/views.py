from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe                #to access Recipes model



# Create your views here.

def welcome(request):
    return render(request, 'recipes/recipes_home.html')

# Create your views here.
class RecipeListView(ListView):           #class-based view
    model = Recipe                         #specify model
    template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(DetailView):                       #class-based view
    model = Recipe                                        #specify model
    template_name = 'recipes/detail.html'                 #specify template