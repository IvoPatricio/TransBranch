from rest_framework import serializers
from .models import User, FriendRequest
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'num_games', 'num_games_won', 'num_tournaments', 'num_tournaments_won']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            num_games=validated_data['num_games'],
            num_games_won=validated_data['num_games_won'],
            num_tournaments=validated_data['num_tournaments'],
            num_tournaments_won=validated_data['num_tournaments_won'],
        )
        
        user.password = make_password(validated_data['password'])
        user.save()
        return user

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['user1', 'user2', 'was_accepted', 'was_canceled', 'was_refused']

    def create(self, validated_data):
        FriendRequest = User.objects.create(
            user1=validated_data['user1'],
            user2=validated_data['user2'],
            was_accepted=validated_data['was_accepted'],
            was_canceled=validated_data['was_canceled'],
            was_refused=validated_data['was_refused'],
        )
        
        FriendRequest.save()
        return FriendRequest
