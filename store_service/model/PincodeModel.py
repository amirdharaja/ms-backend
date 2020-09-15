from django.db import models



class Pincode(models.Model):

    pincode          =   models.IntegerField(null=False, blank=False)
    created_at      =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at     =   models.DateTimeField(auto_now=True, null=True)
    

    objects = models.Manager()

    def __str__(self):
        return 'Pincode: {}'.format(self.pincode)

    class Meta:
        db_table = "pincodes"