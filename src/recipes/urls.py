from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, records
from django.views.generic import RedirectView

app_name = 'recipes'


urlpatterns = [
    path("", RedirectView.as_view(url="home/")),
    path('home/', home, name='home'),
    path('recipes/list/', RecipeListView.as_view(), name='list'),
    path('recipes/list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipes/search', records, name='records')
]