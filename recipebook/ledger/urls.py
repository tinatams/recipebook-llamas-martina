from django.urls import path
from .views import recipe_list, recipe_1

urlpatterns = [
    path('recipes/list', recipe_list, name="index"), 
    path('recipe/1', recipe_1, name="recipe_1"),
]

app_name = "ledger"