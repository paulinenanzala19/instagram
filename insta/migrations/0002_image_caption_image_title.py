# Generated by Django 4.0.5 on 2022-06-04 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]