from django.db import models


class Recipe(models.Model):
    url = models.URLField()
