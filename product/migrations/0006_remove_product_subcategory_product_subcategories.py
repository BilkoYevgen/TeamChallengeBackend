# Generated by Django 5.0.6 on 2024-06-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_subcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategories',
            field=models.ManyToManyField(related_name='products', to='product.subcategory', verbose_name='subcategories'),
        ),
    ]
