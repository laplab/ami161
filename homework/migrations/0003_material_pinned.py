# Generated by Django 2.0 on 2018-01-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20180123_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
