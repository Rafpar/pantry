from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    user_id = models.IntegerField(default=0)
    is_base_product = models.BooleanField(default=False)
    is_optional_product = models.BooleanField(default=False)
    is_custom_product = models.BooleanField(default=False)
    desired_amount = models.IntegerField(default=0)
    current_amount = models.IntegerField(default=0)
    lacking_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
