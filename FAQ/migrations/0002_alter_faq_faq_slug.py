# Generated by Django 4.2.7 on 2024-01-30 16:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='faq_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='ques', unique=True),
        ),
    ]
