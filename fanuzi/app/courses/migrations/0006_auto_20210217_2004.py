# Generated by Django 3.0.6 on 2021-02-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210216_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ссылка на курс'),
        ),
    ]