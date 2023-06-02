# Generated by Django 4.1.7 on 2023-04-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("admins", "0003_syllabus_subtopic"),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="data_from_category",
                to="admins.category",
            ),
        ),
    ]