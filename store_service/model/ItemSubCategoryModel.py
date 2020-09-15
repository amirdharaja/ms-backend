from django.db import models
from django.shortcuts import reverse

from store_service.model.ItemCategoryModel import ItemCategory



class ItemSubCategory(models.Model):

    category        =    models.ForeignKey(ItemCategory, on_delete=models.CASCADE, unique=False)
    name              =    models.CharField(max_length=255, null=False, blank=False)
    slug                =    models.SlugField()
    image              =    models.FileField(upload_to='images/item_sub_category', null=True, default='images/no_image.png',)
    created_at       =    models.DateTimeField(auto_now_add=True, null=True)
    updated_at      =    models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "item_sub_categories"