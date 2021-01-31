from rest_framework import serializers
from .models import Dish, Card, CardItems

class EmenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        #fields = ['name', 'description', 'price', 'preparation_time', 'wege', 'image']
        fields = '__all__'

class EmenuSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        #fields = ['name', 'description']
        fields = '__all__'

class EmenuSerializer3(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardItems
        fields = '__all__'
