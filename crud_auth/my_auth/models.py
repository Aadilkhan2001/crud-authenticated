from django.db import models
from django.contrib.auth.models import User


#model cart
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
