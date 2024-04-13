# Generated by Django 5.0.4 on 2024-04-13 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_recipe_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2024, 4, 13, 12, 21, 36, 660548, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
