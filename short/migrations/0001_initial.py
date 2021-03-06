# Generated by Django 3.2.13 on 2022-04-20 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_uri', models.URLField(max_length=255, verbose_name='Actual URI')),
                ('uri_hash', models.CharField(max_length=10, unique=True, verbose_name='Hash Code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Short URI',
                'verbose_name_plural': 'Shorts URI',
            },
        ),
    ]
