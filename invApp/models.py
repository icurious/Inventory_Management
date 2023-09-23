from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return "Name: {}".format(self.name)


class Sales(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,default='')
    quantity=models.IntegerField()
    total_amount = models.IntegerField()