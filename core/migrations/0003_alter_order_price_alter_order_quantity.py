# Generated by Django 4.1.3 on 2022-11-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_authtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=128),
        ),
    ]