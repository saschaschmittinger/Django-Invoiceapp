# Generated by Django 5.1.3 on 2024-11-28 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_tag_invoice_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='tag',
            new_name='tags',
        ),
    ]