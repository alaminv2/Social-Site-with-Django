# Generated by Django 3.1 on 2020-08-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_auto_20200828_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile_model',
            name='pro_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
