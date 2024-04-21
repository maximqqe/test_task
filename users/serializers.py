import re
from rest_framework import serializers
from .models import CustomUser


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        pattern = r'^\+\d{10,13}$'

        if not re.match(pattern, phone_number):
            raise serializers.ValidationError("неверный номер телефона")

        return attrs


class VerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    code = serializers.IntegerField(min_value=1000, max_value=9999)

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        pattern = r'^\+\d{10,13}$'

        if not re.match(pattern, phone_number):
            raise serializers.ValidationError("неверный номер телефона")

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'invite_code', 'invited_by']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        invited_by = instance.invited_by
        referrals = CustomUser.objects.filter(invited_by=instance.invite_code)
        if referrals:
            phone_numbers = [obj.phone_number for obj in referrals]
            data['referrals'] = phone_numbers

        if invited_by:
            data['invited_by'] = invited_by
        else:
            data.pop('invited_by', None)
        return data




