# Generated by Django 4.2.7 on 2024-03-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipientname', models.CharField(max_length=150)),
                ('recipientphone', models.CharField(max_length=150)),
                ('recipientlocation', models.CharField(max_length=150)),
                ('recipientage', models.CharField(max_length=150)),
                ('recipientgender', models.CharField(max_length=150)),
                ('recipientblood', models.CharField(max_length=150)),
                ('recipientdonationtype', models.CharField(max_length=150)),
                ('recipientdonationquantity', models.CharField(max_length=150)),
                ('recipientcondition', models.CharField(max_length=150)),
                ('recipientdate', models.CharField(max_length=150)),
            ],
        ),
    ]
