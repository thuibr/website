from django.contrib import admin

from recipe.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.reigister(Recipe, RecipeAdmin)
