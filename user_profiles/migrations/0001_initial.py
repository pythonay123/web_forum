# Generated by Django 3.0.5 on 2020-04-23 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('user_level', models.CharField(choices=[('No Level', 'No Level'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold')], default='No Level', max_length=100)),
                ('seniority', models.CharField(choices=[('Newcomer', 'Newcomer'), ('Basic Experience', 'Basic Experience'), ('Intermediate Experience', 'Intermediate Experience'), ('Advanced Experience', 'Advanced Experience')], default='Newcomer', max_length=100)),
                ('number_of_threads_created', models.IntegerField(default=0)),
                ('number_of_posts', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('profile_views', models.IntegerField(default=0)),
                ('admin_message', models.TextField(blank=True, max_length=600, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('summary', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(default='user_profiles/images/default.jpg', null=True, upload_to='user_profiles/images/')),
                ('address_line_1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('street_address', models.TextField(blank=True, max_length=500, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('timezone', models.CharField(default='UTC', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
