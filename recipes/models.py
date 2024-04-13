from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:recipe-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("recipes:recipe-update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("recipes:recipe-delete", kwargs={"pk": self.pk})
