from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    marka = models.CharField(max_length=100)
    model= models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    year= models.SmallIntegerField(default= 0)
    mileage = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    with_photo = models.BooleanField(default=False)
    color = models.CharField(max_length=100)
    volume = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Bet(models.Model):
    number = models.PositiveIntegerField(default=1)
    total_number = models.PositiveIntegerField()
    buy_now = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True )
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)

