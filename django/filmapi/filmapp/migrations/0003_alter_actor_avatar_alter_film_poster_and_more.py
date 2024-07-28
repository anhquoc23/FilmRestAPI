# Generated by Django 5.0.7 on 2024-07-28 08:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0002_film_description_alter_actor_id_alter_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='poster'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
    ]
