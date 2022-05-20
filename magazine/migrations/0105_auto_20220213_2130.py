# Generated by Django 3.2.8 on 2022-02-13 21:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0104_auto_20220128_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='post_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='com_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment_of_comment',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='sub_com_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
