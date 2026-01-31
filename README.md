# Ex01 Django ORM Web Application
## Date: 31.01.2026

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:Execute the migration files and update the database schema to match your Django models
### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class FoodDelivery(models.Model):
      order_id=models.IntegerField(primary_key=True);
      cust_name=models.CharField(max_length=15);
      address=models.CharField(max_length=25);
      order=models.CharField(max_length=20);
      price=models.FloatField();
      mobileno=models.IntegerField();
      deliverycharge=models.FloatField();
class FoodDeliveryAdmin(admin.ModelAdmin):
      list_display=['order_id','cust_name','address','order','price','mobileno','deliverycharge'];

admin.py
from django.contrib import admin
from.models import FoodDeliveryAdmin,FoodDelivery
admin.site.register(FoodDelivery,FoodDeliveryAdmin)

```


## OUTPUT
![alt text](<Screenshot (20).png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
