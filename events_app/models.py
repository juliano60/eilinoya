from django.db import models


# Create your models here.
class Wine(models.Model):
    class Colour(models.TextChoices):
        RED = "RD", "Red"
        WHITE = "WH", "White"

    class Year(models.IntegerChoices):
        YEAR_16 = 1
        YEAR_17 = 2
        YEAR_18 = 3
        YEAR_19 = 4
        YEAR_20 = 5
        YEAR_21 = 6
        YEAR_22 = 7
        YEAR_23 = 8
        YEAR_24 = 9

    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=Colour.choices, default=Colour.RED)
    region = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField(choices=Year.choices, default=Year.YEAR_16)
    alcohol_pct = models.DecimalField(max_digits=3, decimal_places=1)
    preparation = models.CharField(max_length=200, blank=True, default='')
    price = models.IntegerField()
    slogan = models.CharField(max_length=200, blank=True, default='')
    image_url = models.CharField(max_length=100)
    grape_variety = models.CharField(max_length=200)
    cepage = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} | {self.type} | {self.year}'
