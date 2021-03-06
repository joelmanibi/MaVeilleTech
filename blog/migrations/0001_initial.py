# Generated by Django 3.2.5 on 2021-08-01 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('aut_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('subtitle2', models.CharField(blank=True, max_length=200)),
                ('paragraphe2', models.TextField(blank=True)),
                ('subtitle3', models.CharField(blank=True, max_length=200)),
                ('paragraphe3', models.TextField(blank=True)),
                ('subtitle4', models.CharField(blank=True, max_length=200)),
                ('paragraphe4', models.TextField(blank=True)),
                ('subtitle1', models.CharField(blank=True, max_length=200)),
                ('paragraphe1', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
