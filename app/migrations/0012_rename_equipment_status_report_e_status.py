# Generated by Django 4.2.10 on 2024-03-15 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_status_report_equipment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='equipment_status',
            new_name='e_status',
        ),
    ]
