# Generated by Django 5.0.3 on 2024-03-17 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employer', models.CharField(max_length=100)),
                ('Postal_Address', models.CharField(max_length=100)),
                ('Telephone', models.PositiveBigIntegerField()),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admission_No', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=64)),
                ('Other_Names', models.CharField(max_length=64)),
                ('Sex', models.CharField(default='Choose Gender', max_length=10)),
                ('Date_Of_Birth', models.DateField()),
                ('Age', models.PositiveIntegerField()),
                ('Postal_Address', models.CharField(blank=True, max_length=64, null=True)),
                ('Telephone', models.PositiveBigIntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Home_District', models.CharField(max_length=100)),
                ('Subcounty', models.CharField(max_length=100)),
                ('Nationality', models.CharField(max_length=100)),
                ('Occupation', models.CharField(max_length=100)),
                ('Present_Job_TiTle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]