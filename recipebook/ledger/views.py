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


class recipe_add_image(LoginRequiredMixin, CreateView):
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