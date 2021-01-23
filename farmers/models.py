from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class SellerProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)
    delivery_fee = models.DecimalField(max_digits=3, decimal_places=2)
    # latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    # longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])

    def __str__(self):
        return self.shop_name


class Inventory(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, default=1)
    crops = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    quantity = models.DecimalField(decimal_places=3, max_digits=10)
