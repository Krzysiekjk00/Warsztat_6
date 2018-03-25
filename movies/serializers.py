from rest_framework import serializers

from movies.models import Person, Movie


class PersonSerializer(serializers.ModelSerializer):
    model = Person
    fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    model = Movie
    fields = '__all__'
