from django.shortcuts import render

from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = { "recipes": recipes}
    return render(request, 'list.html', context)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = { "recipe" : recipe }

    return render(request, 'recipe.html', context)