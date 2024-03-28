from django.db import models


class Bike(models.Model):
    PAYMENT_MODE = [('ON', 'ONLINE PAYMENT'), ("EMI", "MONTHLY INSTALLMENT")]
    BIKE_QUANTITY = [("moped", 'scooty'), ("pulsure", '150cc'), ("ktm", '200cc')]
    bike_rental_name = models.CharField(max_length=20)
    hour_price = models.IntegerField()
    total_rental_time = models.IntegerField()
    discount_price = models.IntegerField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)
    bike_quantity = models.CharField(max_length=10, choices=BIKE_QUANTITY)


