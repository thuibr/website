import pytest
from django.urls import reverse

from recipes.models import Recipe


@pytest.mark.django_db
def test_recipe_get_absolute_url_maps_to_recipe_detail():
    recipe = Recipe.objects.create(url="https://recipes.com/recipe/")
    expected_url = reverse("recipes:recipe-detail", kwargs={"pk": recipe.pk})

    url = recipe.get_absolute_url()

    assert expected_url == url