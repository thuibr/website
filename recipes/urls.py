from django.urls import path

from .views import RecipeCreateView, RecipeListView, RecipeDetailView, RecipeUpdateView


app_name = "recipes"
urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe-list"),
    path("create/", RecipeCreateView.as_view(), name="recipe-create"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("<int:pk>/edit", RecipeUpdateView.as_view(), name="recipe-update"),
]
