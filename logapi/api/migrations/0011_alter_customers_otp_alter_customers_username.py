# Generated by Django 4.2.5 on 2023-09-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_customers_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='otp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customers',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
