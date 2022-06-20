from django.db import models
from .customer import Customer
from .product import Product
from .category import Category
import datetime


class Lookingfor(models.Model):
	req_product = models.CharField(max_length=255,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
