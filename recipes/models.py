from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("recipes:recipe-detail", kwargs={"pk": self.pk})
