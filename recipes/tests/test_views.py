import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from recipes.models import Recipe


def test_recipe_create_uses_correct_template(admin_client):
    url = reverse("recipes:recipe-create")
    response = admin_client.get(url)
    assertTemplateUsed(response, "recipes/recipe_form.html")


@pytest.mark.django_db
def test_recipe_create_saves_the_url(admin_client):
    url = reverse("recipes:recipe-create")

    response = admin_client.post(url, data={"url": "https://recipes.com/recipe/"})

    assert 302 == response.status_code

    assert Recipe.objects.get().url == "https://recipes.com/recipe/"


@pytest.mark.django_db
def test_recipe_detail_view_status_is_200(client):
    recipe = Recipe.objects.create(url="https://recipes.com/recipe/")
    url = reverse("recipes:recipe-detail", kwargs={"pk": recipe.pk})

    response = client.get(url)

    assert 200 == response.status_code
