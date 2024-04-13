import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from recipes.models import Recipe


def test_recipe_create_uses_correct_template(admin_client):
    url = reverse("recipes:recipe-create")
    response = admin_client.get(url)
    assertTemplateUsed(response, "recipes/recipe_form.html")


@pytest.mark.django_db
def test_recipe_create_redirects(admin_client):
    url = reverse("recipes:recipe-create")

    response = admin_client.post(
        url,
        data={
            "url": "https://recipes.com/recipe/",
            "title": "title",
            "notes": "some notes about the recipe",
        },
    )

    assert 302 == response.status_code


@pytest.mark.django_db
def test_recipe_create_correctly_saves_the_fields(admin_client):
    url = reverse("recipes:recipe-create")

    admin_client.post(
        url,
        data={
            "url": "https://recipes.com/recipe/",
            "title": "title",
            "notes": "some notes about the recipe",
        },
    )

    recipe = Recipe.objects.get()
    assert "https://recipes.com/recipe/" == recipe.url
    assert "title" == recipe.title
    assert "some notes about the recipe" == recipe.notes


@pytest.mark.django_db
def test_recipe_detail_view_status_is_200(client):
    recipe = Recipe.objects.create(url="https://recipes.com/recipe/")
    url = reverse("recipes:recipe-detail", kwargs={"pk": recipe.pk})

    response = client.get(url)

    assert 200 == response.status_code


@pytest.mark.django_db
def test_recipe_update_redirects(admin_client):
    recipe = Recipe.objects.create(
        url="https://recipes.com/recipe/",
        title="title",
        notes="some notes about the recipe",
    )
    url = reverse("recipes:recipe-update", kwargs={"pk": recipe.pk})

    response = admin_client.post(
        url,
        data={
            "url": "https://recipes.com/recipe-modified/",
            "title": "modified title",
            "notes": "some modified notes about the recipe",
        },
    )

    assert 302 == response.status_code


@pytest.mark.django_db
def test_recipe_update_correctly_saves_the_fields(admin_client):
    recipe = Recipe.objects.create(
        url="https://recipes.com/recipe/",
        title="title",
        notes="some notes about the recipe",
    )
    url = reverse("recipes:recipe-update", kwargs={"pk": recipe.pk})

    admin_client.post(
        url,
        data={
            "url": "https://recipes.com/recipe-modified/",
            "title": "modified title",
            "notes": "some modified notes about the recipe",
        },
    )

    recipe = Recipe.objects.get()
    assert "https://recipes.com/recipe-modified/" == recipe.url
    assert "modified title" == recipe.title
    assert "some modified notes about the recipe" == recipe.notes


@pytest.mark.django_db
def test_recipe_delete_redirects(admin_client):
    recipe = Recipe.objects.create(
        url="https://recipes.com/recipe/",
        title="title",
        notes="some notes about the recipe",
    )
    url = reverse("recipes:recipe-delete", kwargs={"pk": recipe.pk})

    response = admin_client.post(
        url,
    )

    assert 302 == response.status_code
