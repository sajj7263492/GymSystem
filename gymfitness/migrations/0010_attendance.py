# Generated by Django 4.2.6 on 2024-04-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymfitness', '0009_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectDate', models.DateTimeField(auto_now_add=True)),
                ('login', models.CharField(max_length=150)),
                ('logout', models.CharField(max_length=150)),
                ('selectWorkout', models.CharField(max_length=150)),
                ('trainedBy', models.CharField(max_length=150)),
            ],
        ),
    ]
