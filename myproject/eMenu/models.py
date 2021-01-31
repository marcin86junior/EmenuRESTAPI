from django.db import models
from django.utils import timezone, dateformat

# Create your models here.

class Card(models.Model):
    name        = models.CharField(max_length=50, verbose_name="Nazwa menu", unique=True, null=True, blank=True)
    description = models.CharField(max_length=500, verbose_name="Opis menu", null=True, blank=True)
    add_time    = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania menu")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Data zmiany menu")

    def __str__(self):
            return self.name

class Dish(models.Model):
    name             = models.CharField(max_length=50, verbose_name="Nazwa dania", unique=True)
    description      = models.CharField(max_length=500, verbose_name="Opis dania")
    price            = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Cena (zł)")
    preparation_time = models.IntegerField(verbose_name="Przygotowanie (min)")
    add_time         = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania przep.")
    update_time      = models.DateTimeField(auto_now=True, verbose_name="Data zmiany przepisu")
    wege             = models.BooleanField(default=True, verbose_name="Wegetariańskie")
    image            = models.ImageField(upload_to='static/', verbose_name='Obrazek', null=True, blank=True)

    def __str__(self):
        return self.name

class CardItems(models.Model):
    card = models.ForeignKey('Card', related_name='card', on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', related_name='dish', on_delete=models.CASCADE)

    def __str__(self):
        return u'%s' % (self.card)