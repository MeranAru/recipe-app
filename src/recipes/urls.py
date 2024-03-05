from django.urls import path
from .views import welcome, records
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', welcome, name='home'),
    path('recipes/', records, name='records'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]