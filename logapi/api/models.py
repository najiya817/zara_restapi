from django.db import models

# Create your models here.
default_status_choice= [
    (True, "active"),
    (False, "inactive"),
]


class Customers(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,unique=True)
    password=models.IntegerField()
    status = models.BooleanField(default=False,choices = default_status_choice)
    session=models.CharField(max_length=50,null=True)
    otp=models.CharField(max_length=50,null=True)

class Category(models.Model):
    ct_id=models.IntegerField(primary_key=True)
    ct_name=models.CharField(max_length=100,unique=True)
    status = models.BooleanField(default=True,choices = default_status_choice)

class Brand(models.Model):
    br_id=models.IntegerField(primary_key=True)
    br_name=models.CharField(max_length=100,unique=True)
    status = models.BooleanField(default=True,choices = default_status_choice)
 
class Products(models.Model):
    pr_id=models.IntegerField(primary_key=True)
    pr_name=models.CharField(max_length=100)
    ct_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    br_id=models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock=models.IntegerField()
    price=models.IntegerField()
    images=models.ImageField(upload_to="product_images")
    status = models.BooleanField(default=True,choices = default_status_choice)


class Banner(models.Model):
    bn_id=models.IntegerField(primary_key=True)
    photo=models.ImageField(upload_to='banner_images')