from rest_framework import serializers
from django.contrib.auth import get_user_model
Account = get_user_model()
import os

class BasicAccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'email',
            'points'
        )

