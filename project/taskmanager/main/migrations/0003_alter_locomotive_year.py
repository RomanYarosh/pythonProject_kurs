# Generated by Django 4.0.5 on 2022-06-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_locomotive_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locomotive',
            name='year',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
    ]
