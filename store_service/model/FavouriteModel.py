from django.db import models
from store_service.models import User

from store_service.model.ItemModel import Item



class Favourite(models.Model):

    user            =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    item             =   models.ForeignKey(Item, on_delete=models.CASCADE, unique=False)
    created_at   =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at  =   models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.user

    class Meta:
        db_table = "favourites"