# Generated by Django 4.1.3 on 2023-02-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_catefood_alter_member_cateplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='social',
            field=models.CharField(max_length=100, null=True, verbose_name='소셜로그인 여부'),
        ),
    ]
