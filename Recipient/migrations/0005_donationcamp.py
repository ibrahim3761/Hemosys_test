# Generated by Django 4.2.7 on 2024-04-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipient', '0004_recipient_recipientemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='donationCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campname', models.CharField(max_length=150)),
                ('campdate', models.CharField(max_length=150)),
                ('camptime', models.CharField(max_length=150)),
                ('campaddress', models.CharField(max_length=150)),
                ('campcontact', models.CharField(max_length=150)),
                ('camporganizer', models.CharField(max_length=150)),
            ],
        ),
    ]