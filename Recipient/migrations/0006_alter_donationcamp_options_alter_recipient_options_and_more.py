# Generated by Django 4.2.7 on 2024-04-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipient', '0005_donationcamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donationcamp',
            options={'verbose_name': 'Organized Camp', 'verbose_name_plural': 'Organized Camp'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'verbose_name': 'Requested Blood', 'verbose_name_plural': 'Requested Blood'},
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='campaddress',
            field=models.CharField(max_length=150, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='campcontact',
            field=models.CharField(max_length=150, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='campdate',
            field=models.CharField(max_length=150, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='campname',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='camporganizer',
            field=models.CharField(max_length=150, verbose_name='Organizer'),
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='camptime',
            field=models.CharField(max_length=150, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientage',
            field=models.CharField(max_length=150, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientblood',
            field=models.CharField(max_length=150, verbose_name='Blood Group'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientcondition',
            field=models.CharField(max_length=150, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientdate',
            field=models.CharField(max_length=150, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientdonationquantity',
            field=models.CharField(max_length=150, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientdonationtype',
            field=models.CharField(max_length=150, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientemail',
            field=models.CharField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientgender',
            field=models.CharField(max_length=150, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientlocation',
            field=models.CharField(max_length=150, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientname',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipientphone',
            field=models.CharField(max_length=150, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='recipienttime',
            field=models.CharField(default=None, max_length=150, verbose_name='Time'),
        ),
    ]
