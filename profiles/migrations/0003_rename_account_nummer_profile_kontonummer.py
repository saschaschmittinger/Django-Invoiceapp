# Generated by Django 5.1.3 on 2024-11-28 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_profil_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='account_nummer',
            new_name='kontonummer',
        ),
    ]