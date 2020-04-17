from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from members.models import User
from members.utils import check_email_hunter


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "username",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                'validators': [UniqueValidator(queryset=User.objects.all())]
            },
        }

    def validate(self, data):
        # we don't create separate validator because we should make api query
        # only after validation another fields and checking email structure
        # for exclude excess api queries
        if not check_email_hunter(data['email']):
            raise serializers.ValidationError({'email': 'Incorrect email'})
        return data

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ClearbitUserSerializer(serializers.ModelSerializer):
    givenName = serializers.CharField(source='first_name')
    familyName = serializers.CharField(source='last_name')
    
    class Meta:
        model = User
        fields = [
            "givenName",
            "familyName",
        ]
