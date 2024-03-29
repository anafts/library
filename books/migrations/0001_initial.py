# Generated by Django 5.0.1 on 2024-01-17 02:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=100)),
                ("pages", models.IntegerField()),
                ("copies", models.IntegerField()),
                ("isbn", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
                ("publishing_company", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
