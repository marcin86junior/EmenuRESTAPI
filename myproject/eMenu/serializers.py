from rest_framework import serializers
from .models import Dish, Card, CardItems
from rest_framework import filters

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

    #def update(self, instance, validated_data):
    #    instance.email = validated_data.get('email', instance.email)
    #    instance.content = validated_data.get('content', instance.content)
    #    instance.created = validated_data.get('created', instance.created)
    #    return instance

