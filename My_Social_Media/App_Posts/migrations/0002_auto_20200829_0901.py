# Generated by Django 3.1 on 2020-08-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='post_pic',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]