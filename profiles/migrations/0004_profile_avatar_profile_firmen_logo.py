# Generated by Django 5.1.3 on 2024-12-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_account_nummer_profile_kontonummer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/avatar.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='firmen_logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]
