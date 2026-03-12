from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Recipe, Profile
from .forms import RecipeForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "list.html", context)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}

    return render(request, "recipe.html", context)

@login_required
def recipe_add(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe()
            recipe.name = form.cleaned_data.get('name')
            recipe.author = form.cleaned_data.get('author')
            recipe.save()

    context = { "form" : form, "profiles" : Profile.objects.all}

    return render(request, "recipe_add.html", context)