# Generated by Django 4.0 on 2024-03-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casterm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profel')),
                ('gender', models.CharField(choices=[('', 'Select Gender'), ('Male', 'Male'), ('Famale', 'Famale')], max_length=16)),
            ],
        ),
    ]
