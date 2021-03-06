# Generated by Django 2.0 on 2018-01-23 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.CharField(max_length=500, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.CharField(max_length=500, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.Subject'),
        ),
        migrations.AddField(
            model_name='deadline',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.Subject'),
        ),
    ]
