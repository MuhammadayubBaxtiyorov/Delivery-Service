from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    data_created = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    CATEGORY = (
        ('InDoor', 'InDoor'),
        ('Out Door', 'OutDoor')
    )
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    price = models.FloatField(null=True)
    data_created = models.DateTimeField(auto_now_add = True, null=True)
    tags = models.ManyToManyField(Tags)

    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('delivered','delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add = True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.products.name