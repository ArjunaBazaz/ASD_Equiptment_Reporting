# Generated by Django 4.2.11 on 2024-03-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_report_admin_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='admin_comment',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
