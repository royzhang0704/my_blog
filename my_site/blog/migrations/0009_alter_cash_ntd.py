# Generated by Django 4.2.15 on 2024-08-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_processsing_fee_stock_processing_fee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='ntd',
            field=models.IntegerField(),
        ),
    ]
