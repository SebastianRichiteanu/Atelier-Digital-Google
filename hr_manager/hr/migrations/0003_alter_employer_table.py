# Generated by Django 3.2.5 on 2021-07-15 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_alter_employer_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employer',
            table='hr_employer',
        ),
    ]