from django.urls import path

from .views import RecipeListView


app_name = "recipes"
urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe-list"),
]

