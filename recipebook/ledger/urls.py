from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list', recipe_list, name="list"), 
    path('<int:pk>/', recipe_detail, name='recipe_detail')
]

app_name = "ledger"