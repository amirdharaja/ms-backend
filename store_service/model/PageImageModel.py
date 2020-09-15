from django.db import models



class PageImage(models.Model):

    image            =    models.FileField(upload_to='images/page_images', null=False)

    objects = models.Manager()

    class Meta:
        db_table = "page_images"