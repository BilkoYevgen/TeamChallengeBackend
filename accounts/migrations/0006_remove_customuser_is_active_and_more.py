# Generated by Django 5.0.6 on 2024-06-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_customuser_created_at_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_staff",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]