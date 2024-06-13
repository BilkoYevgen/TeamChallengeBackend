# Generated by Django 5.0.6 on 2024-06-11 02:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_customuser_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="customuser",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="Пароль"),
        ),
    ]