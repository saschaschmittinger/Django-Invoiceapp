# Generated by Django 5.1.3 on 2024-12-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]