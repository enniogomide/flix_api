from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):  # tem que começar com validate_
        if value.year < 1900:
            raise serializers.ValidationError('Release date must be after 1990')
        return value

    def validate_resume(self, value):  # tem que começar com validate_
        if len(value) > 2000:
            raise serializers.ValidationError('Resumo tem que ser menor que 200 caracteres')
        return value


class MovieListDetailedSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'released_date', 'rate', 'resume']

    def get_rate(self, obj):  # o get na frente é para identificar que é um campo calculado, definido acima.
        return round(obj.reviews.aggregate(Avg('stars'))['stars__avg'] or 0, 1)


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField(child=serializers.DictField())
    total_reviews = serializers.IntegerField()
    total_reviews_by_movie = serializers.ListField(child=serializers.DictField())
    average_stars = serializers.FloatField()
