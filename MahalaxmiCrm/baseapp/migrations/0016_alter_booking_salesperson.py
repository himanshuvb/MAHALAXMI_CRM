# Generated by Django 4.0.3 on 2022-04-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0015_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='salesperson',
            field=models.CharField(max_length=300),
        ),
    ]
