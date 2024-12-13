# Generated by Django 5.0.2 on 2024-12-07 20:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('hospital', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='doctor_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='doctor_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50)),
                ('profile_picture', models.ImageField(upload_to='images')),
                ('patient_email', models.EmailField(default='default@example.com', max_length=50)),
                ('patient_key', models.CharField(default='notdefined', max_length=10)),
                ('care_taker_email1', models.EmailField(default='default@example.com', max_length=50)),
                ('care_taker_email2', models.EmailField(default='default@example.com', max_length=50)),
                ('doctor_email', models.EmailField(default='default@example.com', max_length=50)),
                ('diseases', models.ManyToManyField(to='heartApp.disease')),
                ('doctor', models.ManyToManyField(to='heartApp.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('altitude', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('timestamp', models.DateTimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='heartApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ECG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecg_data', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='ECG Data')),
                ('timestamp', models.DateTimeField(help_text='Timestamp with microsecond precision', verbose_name='Timestamp')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecg_readings', to='heartApp.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'ECG Reading',
                'verbose_name_plural': 'ECG Readings',
                'ordering': ['-timestamp'],
            },
        ),
    ]