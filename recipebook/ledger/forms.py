from django import forms

from .models import Recipe, Profile

class RecipeForm(forms.ModelForm):
    #name = forms.CharField(label="Recipe Name", max_length=50)
    #author = forms.ModelChoiceField(label='Author', queryset=Profile.objects.all())
    class Meta:
        model = Recipe
        fields = "__all__"