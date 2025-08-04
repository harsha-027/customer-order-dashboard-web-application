from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    traffic_source = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    status = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    num_of_item = models.IntegerField()

    def __str__(self):
        return f"Order {self.order_id} - Status: {self.status}"

