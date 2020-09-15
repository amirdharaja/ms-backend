from django.db import models
from store_service.models import User

from store_service.model.BlogModel import Blog


class BlogComment(models.Model):

    user            =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    blog             =   models.ForeignKey(Blog, on_delete=models.CASCADE, unique=False)
    comment      =   models.CharField(max_length=512, blank=False)
    created_at    =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at   =   models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return 'Blog: {}'.format(self.user)

    class Meta:
        db_table = "blog_comments"
