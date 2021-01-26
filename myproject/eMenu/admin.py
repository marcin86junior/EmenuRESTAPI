from django.contrib import admin
from .models import Dish, Card, CardItems

# Register your models here.

admin.site.register(Dish)
admin.site.register(Card)
admin.site.register(CardItems)