from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=True)
    staff_member = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=100, required=True)