from django.db import models



class SubSlideImage(models.Model):

    image            =    models.FileField(upload_to='images/sub_slide_images', null=False, default='images/no_image.png',)
    is_available    =    models.BooleanField(default=True)
    created_at      =    models.DateTimeField(auto_now_add=True, null=True)
    updated_at     =    models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()


    class Meta:
        db_table = "sub_slide_images"