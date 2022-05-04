# Generated by Django 4.0.3 on 2022-05-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0017_add_sites'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUps_Telecaller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=200, unique=True)),
                ('followUp_By', models.CharField(max_length=200)),
                ('followUp_date', models.DateField()),
                ('remarks', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Visit_Telecaller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('site_details', models.CharField(max_length=500)),
                ('visit_date', models.DateField()),
                ('remarks', models.CharField(max_length=300)),
            ],
        ),
    ]
