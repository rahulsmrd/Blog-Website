# Generated by Django 4.1.4 on 2023-07-13 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0003_rename_pic_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headding', models.CharField(max_length=100)),
                ('upload_File', models.FileField(upload_to='posts')),
                ('is_it_a_Image', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_on', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=1000)),
                ('published_date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('user_comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.posts')),
            ],
        ),
    ]
