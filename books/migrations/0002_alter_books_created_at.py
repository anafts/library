# Generated by Django 5.0.1 on 2024-01-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
