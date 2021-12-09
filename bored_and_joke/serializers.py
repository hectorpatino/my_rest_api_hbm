from rest_framework import serializers

from bored_and_joke.models import BoredAndJoke


class BoredAndJokeForGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoredAndJoke
        exclude = ['id']
        extra_kwargs = {
            'type': {'write_only': True},
            'key': {'write_only': True},
        }


class BoredAndJokeForCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoredAndJoke
        fields = '__all__'
