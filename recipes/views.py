from django.views.generic.list import ListView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe

