# Generated by Django 3.0.6 on 2021-02-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210217_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Ссылка на курс'),
        ),
    ]
