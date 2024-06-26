# Generated by Django 4.2.7 on 2024-04-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_email_contact_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.CharField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_subject',
            field=models.CharField(max_length=200, verbose_name='Subject'),
        ),
    ]
