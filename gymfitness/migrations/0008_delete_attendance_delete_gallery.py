# Generated by Django 4.2.6 on 2024-03-31 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymfitness', '0007_alter_enrollment_fullname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
