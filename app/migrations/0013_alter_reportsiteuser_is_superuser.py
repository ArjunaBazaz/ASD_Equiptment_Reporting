# Generated by Django 4.2.11 on 2024-03-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_equipment_status_report_e_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsiteuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
