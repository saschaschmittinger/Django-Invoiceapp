# Generated by Django 5.1.3 on 2024-11-30 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_rename_tag_invoice_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='tags',
        ),
    ]
