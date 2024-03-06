from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe                #to access Recipes model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart



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
    # create an instance of RecipesSearchForm that you defined in recipes/forms.py
    form = RecipesSearchForm(request.POST or None)
    recipes_df = None  # initialize dataframe to None
    chart = None

# check if the button is clicked
    if request.method == 'POST':
        # read recipe_title and chart_type
        recipe_title = request.POST.get('recipe_title')
        chart_type = request.POST.get('chart_type')

        qs = Recipe.objects.filter(name=recipe_title)
        if qs:  # if data found
            # convert the queryset values to pandas dataframe
            recipes_df = pd.DataFrame(qs.values('id', 'cooking_time', 'difficulty', 'ingredients', 'name', 'pic'))
            recipes_df['id'] = recipes_df['id'].apply(get_recipename_from_id)
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
            recipes_df = recipes_df.to_html()


        '''
        print('Exploring querysets:')
        print('Case 1: Output of Recipe.objects.all()')
        qs = Recipe.objects.all()
        print(qs)

        print('Case 2: Output of Recipe.objects.filter(recipe_name=recipe_title)')
        print(qs)

        print('Case 3: Output of qs.values')
        print(qs.values())

        print('Case 4: Output of qs.values_list()')
        print(qs.values_list())

        print('Case 5: Output of Recipe.objects.get(id=1)')
        obj = Recipe.objects.get(id=1)
        print(obj)
        '''

    #pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipes_df': recipes_df,  # recipes_df initialized here
        'chart': chart
    }

    #load the recipes/record.html page using the data that you just prepared
    return render(request, 'recipes/records.html', context)