# Generated by Django 5.0.6 on 2024-06-22 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_subcategory_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together=set(),
        ),
    ]
