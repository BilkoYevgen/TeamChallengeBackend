from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('name'), max_length=80)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f'{self.name}'


class SubCategory(models.Model):
    name = models.CharField(_('name'), max_length=80)
    category = models.ForeignKey(
        Category, verbose_name=_('category name'), related_name='subcategories', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    price = models.DecimalField(_('price'), default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image_urls = models.TextField(_('image URLs'), help_text=_("Enter image URLs separated by commas."))
    subcategories = models.ManyToManyField(SubCategory, verbose_name=_('subcategories'), related_name='products')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_product_name')
        ]

    def __str__(self):
        return self.name
