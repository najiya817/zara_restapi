# Generated by Django 4.2.5 on 2023-09-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_brand_status_alter_category_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='status',
            field=models.BooleanField(choices=[(True, 'active'), (False, 'inactive')], default=False),
        ),
    ]