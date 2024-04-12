from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("recipes:recipe-detail", kwargs={"pk": self.pk})
