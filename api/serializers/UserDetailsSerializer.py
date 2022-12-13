from collections import OrderedDict

from api.models import AppUser
from rest_framework import serializers


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = (
            'pk',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'city',
            'country',
            'balance'
        )

    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if self.ok(result[key])])

    # noinspection PyMethodMayBeStatic
    def ok(self, s):
        if type(s) is list:
            return len(s) > 0
        if s == "":
            return False
        return s is not None
