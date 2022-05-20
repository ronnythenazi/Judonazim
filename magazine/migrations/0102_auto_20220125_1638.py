# Generated by Django 3.2.8 on 2022-01-25 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0101_auto_20220125_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='post_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes_com', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_com', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment_of_comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes_com_of_com', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment_of_comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_com_of_com', to=settings.AUTH_USER_MODEL),
        ),
    ]
