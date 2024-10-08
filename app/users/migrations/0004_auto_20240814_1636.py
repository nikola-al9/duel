# Generated by Django 3.2.11 on 2024-08-14 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240814_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationTokenEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('token', models.UUIDField(default=uuid.uuid4)),
                ('is_expired', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'registration_token_email',
            },
        ),
        migrations.RemoveField(
            model_name='account',
            name='reg_token',
        ),
        migrations.RemoveField(
            model_name='account',
            name='reg_token_is_expired',
        ),
    ]
