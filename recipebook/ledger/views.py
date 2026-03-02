from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "list.html", context)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}

    return render(request, "recipe.html", context)
