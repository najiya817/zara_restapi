# Generated by Django 4.2.5 on 2023-09-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customers_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customers',
            name='session',
            field=models.IntegerField(),
        ),
    ]
