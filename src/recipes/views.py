from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe                #to access Recipes model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required



# Create your views here.

def welcome(request):
    return render(request, 'recipes/recipes_home.html')

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):           #class-based view
    model = Recipe                         #specify model
    template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based view
    model = Recipe                                        #specify model
    template_name = 'recipes/detail.html'                 #specify template

#define function-based view - records(records()
@login_required
def records(request):
    #do nothing, simply display page    
    return render(request, 'recipes/records.html')