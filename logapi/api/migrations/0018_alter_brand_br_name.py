# Generated by Django 4.2.5 on 2023-09-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_category_ct_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='br_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]