# Generated by Django 4.2.7 on 2024-04-28 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0004_add_faq_delete_faq'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_faq',
            new_name='faq',
        ),
    ]
