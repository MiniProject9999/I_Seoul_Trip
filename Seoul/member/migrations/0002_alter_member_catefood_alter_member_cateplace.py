# Generated by Django 4.1.4 on 2023-01-31 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cateFood',
            field=models.CharField(max_length=255, verbose_name='선호하는 음식'),
        ),
        migrations.AlterField(
            model_name='member',
            name='catePlace',
            field=models.CharField(max_length=255, verbose_name='선호하는 장소'),
        ),
    ]
