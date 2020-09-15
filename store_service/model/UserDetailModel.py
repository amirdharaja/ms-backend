from django.db import models
from store_service.models import User



class UserDetail(models.Model):

    ROLE = (
        ('', u''),
        ('User', u'User'),
        ('Admin', u'Admin'),
        ('Super Admin', u'Super Admin'),
        ('Delivery Boy', u'Delivery Boy'),
    )

    user              =    models.OneToOneField(User, on_delete=models.CASCADE)
    role               =    models.CharField(choices=ROLE, max_length=16, null=False, default='User')
    email             =    models.EmailField(null=True)
    email_verified =    models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    created_at       =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at      =   models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return 'User Detail: {}'.format(self.user)

    class Meta:
        db_table = "user_details"
