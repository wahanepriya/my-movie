from rest_framework import serializers

from movie_app.models import Movies, MovieGenre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'


class MoviesSerializers(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, source='get_all_movie_genre')

    class Meta:
        model = Movies
        fields = (
            'id',
            'imdb_score',
            'genre',
            'director',
            'popularity_99',
            'name'
        )


class MoviesRetrieveSerializers(serializers.ModelSerializer):
    genre = GenreSerializer(many=True,source='get_all_movie_genre')

    class Meta:
        model = Movies
        fields = (
            'id',
            'imdb_score',
            'genre',
            'director',
            'popularity_99',
            'name'
        )

