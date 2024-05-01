# Generated by Django 4.2.11 on 2024-03-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_reportsiteuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='common_issue',
            field=models.CharField(choices=[('1', 'N/A'), ('2', 'Water Fountain Filter'), ('3', 'Clogging in Bathroom'), ('4', 'Bathroom Supply'), ('5', 'Classroom Equipment')], default='1', max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='e_status',
            field=models.CharField(choices=[('1', 'Functioning'), ('2', 'Problematic'), ('3', 'Unusable')], default='1', max_length=15),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_status',
            field=models.CharField(choices=[('1', 'Not Addressed'), ('2', 'In Progress'), ('3', 'Addressed')], default='1', max_length=15),
        ),
    ]
