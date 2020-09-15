from django.db import models

from store_service.model.ItemModel import Item



class SpecialItem(models.Model):

    item               =   models.ForeignKey(Item, on_delete=models.CASCADE, unique=False)
    image             =   models.FileField(upload_to='images/spl_items_images', null=True, default='images/no_image.png',)
    date               =   models.DateField(null=True)
    title                =   models.CharField(max_length=128, null=True)
    description      =   models.CharField(max_length=256, null=True)
    created_at      =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at     =   models.DateTimeField(auto_now=True, null=True)


    objects = models.Manager()

    def __str__(self):
        return 'Special Item: "{}"'.format(self.item)

    class Meta:
        db_table = "special_items"