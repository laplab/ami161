# Generated by Django 2.0 on 2018-01-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_material_pinned'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='router_specifications')),
            ],
        ),
    ]
