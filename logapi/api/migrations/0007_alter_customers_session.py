# Generated by Django 4.2.5 on 2023-09-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customers_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='session',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
