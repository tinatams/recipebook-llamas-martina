from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Recipe, RecipeIngredient, RecipeImage


class RecipeImageInline(admin.StackedInline):
    model = RecipeImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeIngredientInline, RecipeImageInline,
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.
