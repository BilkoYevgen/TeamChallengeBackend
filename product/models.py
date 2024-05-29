from django.db import models

from django.utils.translation import gettext_lazy as _  # for i18n by rosetta


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
