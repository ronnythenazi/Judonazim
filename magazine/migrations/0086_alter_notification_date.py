# Generated by Django 3.2.8 on 2022-01-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0085_alter_notification_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default='2022-39-01/20/22 14:39:24'),
        ),
    ]
