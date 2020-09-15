from django.db import models
from store_service.models import User

from store_service.model.OrderModel import Order



class OrderHistory(models.Model):

    STATUS = [
	    ('', u'-------'),
        ('Pending', u'Pending'),
   	    ('Confirmed', u'Confirmed'),
        ('Out for Delivery', u'Out for Delivery'),
   	    ('Delivered', u'Delivered'),
   	    ('Canceled by User', u'Canceled by User'),
   	    ('Canceled by Admin', u'Canceled by Admin'),
	]

    user                =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    order               =   models.ForeignKey(Order, on_delete=models.CASCADE, unique=False)
    created_at        =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at       =   models.DateTimeField(auto_now=True, null=True)


    objects = models.Manager()

    def __str__(self):
        return 'Order by the User ID: {}'.format(self.user)

    class Meta:
        db_table = "order_histories"