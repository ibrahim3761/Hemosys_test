# Generated by Django 3.2.1 on 2024-05-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_alter_bloodbank_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]