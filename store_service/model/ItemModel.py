from django.db import models
from django.shortcuts import reverse

from store_service.model.ItemSubCategoryModel import ItemSubCategory



class Item(models.Model):

    DIVIDE_BY = [
	    ('', u'-------'),
        ('1', u'No Divide'),
   	    ('2', u'Divide By 2'),
        ('4', u'Divide By 4'),
	]

    WEIGHT = [
	    ('', u'-------'),
        (0.0, u'Other'),
        (0.025, u'25 G'),
        (0.050, u'50 G'),
        (0.100, u'100 G'),
        (0.150, u'150 G'),
        (0.200, u'200 G'),
        (0.250, u'250 G'),
        (0.500, u'500 G'),
        (1, u'1 KG'),
        (1.250, u'1.25 KG'),
        (1.500, u'1.50 KG'),
        (2, u'2 KG'),
        (5, u'5 KG'),
        (10, u'10 KG'),
        (15, u'15 KG'),
        (20, u'20 KG'),
        (25, u'25 KG'),
        (50, u'50 KG'),
        (100, u'100 KG'),
	]
    DISCOUNT_TYPE = [
        (0, u'No discount'),
        ('%', u'%'),
        ('₹', u'₹')
    ]

    sub_category        =    models.ForeignKey(ItemSubCategory, on_delete=models.CASCADE, unique=False, null=False)
    name            =    models.CharField(max_length=255, null=False, blank=False, default='item')
    weight         =   models.FloatField(choices=WEIGHT, max_length=8, default=0.0)
    slug              =    models.SlugField()
    image            =    models.FileField(upload_to='images/item_images', null=True, default='images/no_image.png',)
    is_available    =    models.BooleanField(default=True)
    rate  =    models.CharField(null=False, max_length=128)
    discount_type = models.CharField(choices=DISCOUNT_TYPE, max_length=1, default=0)
    discount        =    models.IntegerField(default=0)
    divide_by         =   models.CharField(choices=DIVIDE_BY, max_length=1, default='1')
    description      =    models.TextField(null=True)
    total_sales_count        =    models.IntegerField(editable=False, default=0)
    total_sales_amount        =    models.IntegerField(editable=False, default=0)
    created_at      =    models.DateTimeField(auto_now_add=True, null=True)
    updated_at     =    models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
    class Meta:
        db_table = "items"