# Generated by Django 4.2.1 on 2024-04-06 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_employee_employees'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employees',
            new_name='Employee',
        ),
    ]
