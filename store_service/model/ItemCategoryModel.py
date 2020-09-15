from django.db import models
from django.shortcuts import reverse



class ItemCategory(models.Model):

    name              =    models.CharField(max_length=255, null=False, blank=False)
    slug                =    models.SlugField(null=False, blank=False, unique=True)
    image              =    models.FileField(upload_to='images/item_category', default='images/no_image.png', null=True)
    created_at       =    models.DateTimeField(auto_now_add=True, null=True)
    updated_at      =    models.DateTimeField(auto_now=True, null=True)
    

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "item_categories"
