from django.db import models

# Create your models here.
from movie_app.models import DateBaseModel


class AllUser(DateBaseModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
