from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Recipe, Profile, RecipeImage
from .forms import RecipeForm, RecipeAddImageForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "list.html", context)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}

    return render(request, "recipe.html", context)


class RecipeAdd(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_add.html"
    success_url = "/recipes/list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = Profile.objects.all()
        context["form"] = RecipeForm()
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RecipeAddImage(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeAddImageForm
    template_name = "recipe_add_image.html"

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    
    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)