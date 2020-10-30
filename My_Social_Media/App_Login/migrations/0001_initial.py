# Generated by Django 3.1 on 2020-08-27 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=14)),
                ('dob', models.DateField()),
                ('website', models.URLField(blank=True)),
                ('fb_acc', models.URLField(blank=True)),
                ('pro_pic', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='up_model_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
