from rest_framework import serializers
from .models import Movie, Actor, Review


class MovieSerializer_title(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer_title(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('article',)

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ActorListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer_title(many=True, read_only=True)
    # movie_set = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializer_name(serializers.ModelSerializer):
    # movies = MovieSerializer_title(many=True, read_only=True)
    # movie_set = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Actor
        fields = ('name',)

class ReviewSerializer_title_content(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)
        # read_only_fields = ('article',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer_name(many=True, read_only=True)
    review_set = ReviewSerializer_title_content(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer_ALL(serializers.ModelSerializer):
    movie = MovieSerializer_title(read_only = True)
    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('article',)