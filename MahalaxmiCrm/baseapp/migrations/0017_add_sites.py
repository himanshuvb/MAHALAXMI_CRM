# Generated by Django 4.0.3 on 2022-04-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0016_alter_booking_salesperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to=None)),
                ('property_type', models.CharField(choices=[('Villa', 'Villa'), ('1 BHK', '1 BHK'), ('2 BHK', '2 BHK'), ('3 BHK', '3 BHK'), ('Office', 'Office')], max_length=200)),
                ('location', models.CharField(max_length=500)),
            ],
        ),
    ]
