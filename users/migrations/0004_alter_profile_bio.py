# Generated by Django 4.0.5 on 2022-06-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_bio_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=100),
        ),
    ]
