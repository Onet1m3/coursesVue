# Generated by Django 3.0.6 on 2021-01-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='raiting',
            field=models.PositiveIntegerField(default=0, verbose_name='Рэйтинг курса'),
        ),
    ]
