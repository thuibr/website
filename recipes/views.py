from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ("id", "url", "title", "notes")


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ("id", "url", "title", "notes")


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes:recipe-list")
