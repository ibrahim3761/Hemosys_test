# Generated by Django 4.2.7 on 2024-03-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_userprofile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]