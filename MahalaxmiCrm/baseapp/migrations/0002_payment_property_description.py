# Generated by Django 4.0.1 on 2022-03-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='property_description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
