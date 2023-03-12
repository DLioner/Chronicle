from rest_framework import serializers
from django.contrib.auth import get_user_model


class RegistrationSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'sex',
            'date_of_birth',
            'address',
        )
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('password',)


class UserSerializer(serializers.ModelSerializer):
    address = serializers.CharField()
    last_name = serializers.CharField()

    def update(self, instance, validated_data):
        for attribute in instance.__dict__.keys():
            instance.__dict__.update({
                attribute: validated_data.get(
                    attribute,
                    instance.__dict__.get(attribute))
            })
        instance.save()
        return instance

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'sex',
            'date_of_birth',
            'address',
            'last_name'
        )