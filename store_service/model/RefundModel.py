from django.db import models
from store_service.model.OrderModel import Order

class Refund(models.Model):

    STATUS = [
	    ('', u'-------'),
        ('Pending', u'Pending'),
   	    ('Paid', u'Paid'),
	]

    order       =    models.ForeignKey(Order, on_delete=models.CASCADE, unique=False)
    reason     =    models.TextField()
    status      =    models.CharField(choices=STATUS, max_length=32, default='pending')

    objects = models.Manager()

    def __str__(self):
        return 'Refund: {}'.format(self.order)

    class Meta:
        db_table = "refunds"