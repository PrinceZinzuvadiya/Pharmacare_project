from django.db import models

# Create your models here.
class admins(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.EmailField()
    password=models.CharField(max_length=20)

class manager(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    pharmacy_name=models.CharField(max_length=20)

class medicine(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    Qty=models.CharField(max_length=50)
    price=models.BigIntegerField()
    added_date=models.DateField(auto_now_add=True)
