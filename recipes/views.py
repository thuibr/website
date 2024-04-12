from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ("id", "url")


class RecipeDetailView(DetailView):
    model = Recipe
