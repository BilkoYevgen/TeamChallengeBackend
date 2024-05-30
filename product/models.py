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
        Category, verbose_name=_('category name'), related_name='categories', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    image_urls = models.TextField(_('image URLs'), help_text=_("Enter image URLs separated by commas."))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class ProductSubCategory(models.Model):
    subcategory = models.ForeignKey(SubCategory, verbose_name=_('subcategory'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Product Subcategory')
        verbose_name_plural = _('Product Subcategories')

    def __str__(self):
        return f"{self.subcategory.name} - {self.product.name}"
