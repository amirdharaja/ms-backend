from django.db import models
from store_service.models import User

from store_service.model.BlogModel import Blog



class BlogLike(models.Model):

    user              =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    blog              =   models.ForeignKey(Blog, on_delete=models.CASCADE, unique=False)
    is_like           =   models.BooleanField(default=None)
    created_at     =   models.DateTimeField(auto_now_add=True, null=True)
    updated_at     =   models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return 'Likes for Blog ID: {}'.format(self.blog)

    class Meta:
        db_table = "blog_likes"