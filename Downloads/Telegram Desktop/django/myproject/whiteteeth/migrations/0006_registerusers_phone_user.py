# Generated by Django 5.0.6 on 2024-06-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiteteeth', '0005_appointment_patient_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerusers',
            name='phone_user',
            field=models.CharField(default=1200473319, max_length=100),
            preserve_default=False,
        ),
    ]
