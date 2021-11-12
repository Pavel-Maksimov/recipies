# Generated by Django 3.2.8 on 2021-11-09 06:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_auto_20211108_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='Время приготовления должна быть больше нуля.')], verbose_name='Время приготовления (в минутах)'),
        ),
    ]