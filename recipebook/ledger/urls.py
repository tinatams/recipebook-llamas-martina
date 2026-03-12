from django.urls import path
from .views import recipe_list, recipe_detail, RecipeAdd, RecipeAddImage

urlpatterns = [
    path("recipes/list", recipe_list, name="list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path("recipe/<int:pk>/add_image", RecipeAddImage.as_view(), name="recipe_add_image"),
    path("recipe/add", RecipeAdd.as_view(), name="recipe_add")
]

app_name = "ledger"
