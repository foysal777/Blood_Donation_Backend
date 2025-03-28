# Generated by Django 5.0.6 on 2025-03-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('donor_position', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('blood_group', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('donation_place', models.CharField(max_length=255)),
                ('image_url', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
