# Generated by Django 4.1.7 on 2023-04-26 05:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.TextField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("content", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=blog.models.File
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("created_by", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
