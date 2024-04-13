import pytest
from django.urls import reverse

from recipes.models import Recipe


@pytest.mark.django_db
def test_recipe_get_absolute_url_maps_to_recipe_detail():
    recipe = Recipe.objects.create(url="https://recipes.com/recipe/")
    expected_url = reverse("recipes:recipe-detail", kwargs={"pk": recipe.pk})

    url = recipe.get_absolute_url()

    assert expected_url == url


@pytest.mark.django_db
def test_recipe_get_update_url_maps_to_recipe_update():
    recipe = Recipe.objects.create(url="https://recipes.com/recipe/")
    expected_url = reverse("recipes:recipe-update", kwargs={"pk": recipe.pk})

    url = recipe.get_update_url()

    assert expected_url == url


@pytest.mark.django_db
def test_recipe_get_delete_url_maps_to_recipe_delete():
    recipe = Recipe.objects.create(url="https://recipes.com/recipe/")
    expected_url = reverse("recipes:recipe-delete", kwargs={"pk": recipe.pk})

    url = recipe.get_delete_url()

    assert expected_url == url
