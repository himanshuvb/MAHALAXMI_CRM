# Generated by Django 4.0.3 on 2022-05-04 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0018_followups_telecaller_visit_telecaller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit_telecaller',
            old_name='name',
            new_name='employee_name',
        ),
    ]
