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

