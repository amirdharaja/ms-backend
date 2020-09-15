from django.db import models
from store_service.models import User

from store_service.model.ItemModel import Item
from store_service.model.OrderModel import Order


class Cart(models.Model):

    user            =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    item             =   models.ForeignKey(Item, on_delete=models.CASCADE, unique=False)
    weight          =   models.FloatField()
    count           =   models.IntegerField()
    is_ordered     =   models.BooleanField(default=False)
    order             =   models.ForeignKey(Order, on_delete=models.CASCADE, unique=False, null=True)
    rate        =   models.IntegerField()
    created_at   =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at  =   models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return 'Cart for the User ID: {}'.format(self.user)

    def get_total_item_rate(self):
        return self.count * self.amount

    class Meta:
        db_table = "carts"