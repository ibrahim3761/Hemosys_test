# Generated by Django 4.2.7 on 2024-01-30 15:40

import autoslug.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=50)),
                ('ans', tinymce.models.HTMLField()),
                ('faq_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True)),
            ],
        ),
    ]
