# Generated by Django 4.1.4 on 2023-07-13 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_rename_is_it_a_image_posts_is_it_an_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='published_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]