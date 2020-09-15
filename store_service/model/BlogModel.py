from django.db import models
from store_service.models import User



class Blog(models.Model):

    title                   =   models.CharField(max_length=128, blank=False)
    image               =   models.FileField(upload_to='images/blog_images', default='images/no_image.png', null=True)
    content             =   models.TextField(null=True)
    user                 =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    created_at        =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at        =   models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return 'Blog: {}'.format(self.title)

    class Meta:
        db_table = "blogs"
