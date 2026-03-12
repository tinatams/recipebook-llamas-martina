from django.urls import path
from .views import recipe_list, recipe_detail, recipe_add, recipe_add_image

urlpatterns = [
    path("recipes/list", recipe_list, name="list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path("recipe/add", recipe_add, name="recipe_add"),
    path("recipe/<int:pk>/add_image", recipe_add_image.as_view(), name="recipe_add_image")
]

app_name = "ledger"
