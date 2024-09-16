from rest_framework import serializers

class CheckIntPkSerializer(serializers.Serializer):
    pk = serializers.IntegerField()