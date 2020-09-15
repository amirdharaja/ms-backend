from django.db import models
from store_service.models import User


class LoginHistory(models.Model):

    user          =   models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    created_at =   models.DateTimeField(auto_now_add=True, null=True)

    objects = models.Manager()


    class Meta:
        db_table = "login_history"