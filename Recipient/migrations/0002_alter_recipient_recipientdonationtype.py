# Generated by Django 4.2.7 on 2024-03-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='recipientdonationtype',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
