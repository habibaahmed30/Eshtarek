from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        module =CustomUser('id','username','email','password','tenant','role')

    def create(self,validated_date):
            password=validated_date.pop('password')
            user=CustomUser(**validated_date)
            user.set_password(password)
            user.save()
            return user