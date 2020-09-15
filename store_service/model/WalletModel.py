from django.db import models
from store_service.models import User


class Wallet(models.Model):

    user            =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    balance       =   models.IntegerField(default=0)
    created_at   =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at  =   models.DateTimeField(auto_now=True, null=True)


    objects = models.Manager()

    def __str__(self):
        return 'Wallet: User ID {}'.format(self.user)

    class Meta:
        db_table = "wallets"