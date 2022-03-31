# Generated by Django 4.0.3 on 2022-03-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=None)),
                ('project_description', models.CharField(max_length=1000)),
                ('project_area', models.IntegerField(default=0)),
            ],
        ),
    ]