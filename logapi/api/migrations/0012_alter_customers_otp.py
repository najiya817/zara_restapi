# Generated by Django 4.2.5 on 2023-09-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_customers_otp_alter_customers_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='otp',
            field=models.IntegerField(null=True),
        ),
    ]
