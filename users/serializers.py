from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
  
    def create(self, validated_data):
       return User.objects.create_user(**validated_data)
    
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'artistic_name',
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {"password": {"write_only": True}}



    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    

   

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)

        for key, value in validated_data.items():
            if key== 'password':
                instance.set_password(value)
            else:
                setattr(instance,key,value)

        instance.save()

        return instance
  

