# Generated by Django 4.0.5 on 2022-06-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
