# Generated by Django 5.1.4 on 2024-12-30 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
