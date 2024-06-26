# Generated by Django 4.0 on 2024-02-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('', 'Select your gender'), ('male', 'male'), ('famale', 'famale')], max_length=16)),
                ('birthdate', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(upload_to='profile_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='auth.user')),
            ],
        ),
    ]
