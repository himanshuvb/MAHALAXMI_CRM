# Generated by Django 4.0.3 on 2022-03-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0009_rename_properties_type_property_type_properties_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(max_length=200)),
            ],
        ),
    ]
