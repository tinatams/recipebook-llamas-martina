from django.urls import path
from .views import recipe_list, recipe_detail, recipe_add

urlpatterns = [
    path("recipes/list", recipe_list, name="list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path("recipe/add", recipe_add, name="recipe_add")
]

app_name = "ledger"
