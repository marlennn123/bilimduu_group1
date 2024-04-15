from rest_framework import serializers

from .models import *


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    marka = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    price = serializers.IntegerField(default=0)
    year = serializers.IntegerField(default=0)
    mileage = serializers.IntegerField(default=0)
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    with_photo = serializers.BooleanField(default=False)
    color = serializers.CharField(max_length=100)
    volume = serializers.FloatField(default=0.0)

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        return Car.objects.create(**validated_data)


class BetSerializer(serializers.Serializer):
    number = serializers.IntegerField(default=1)
    total_number = serializers.IntegerField()
    buy_now = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    class Meta:
        model = Bet
        fields = '__all__'

