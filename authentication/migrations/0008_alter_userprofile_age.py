# Generated by Django 4.2.7 on 2024-03-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_userprofile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.CharField(max_length=4),
        ),
    ]