# Generated by Django 4.2.5 on 2023-09-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.IntegerField(null=True),
        ),
    ]
