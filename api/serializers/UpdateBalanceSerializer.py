from rest_framework import serializers


class UpdateBalanceSerializer(serializers.Serializer):
    balance = serializers.DecimalField(decimal_places=3, max_digits=12)
    email = serializers.EmailField(required=True)
    
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

