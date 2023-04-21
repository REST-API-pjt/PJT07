from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Actor, Review
from .serializers import ActorListSerializer, MovieListSerializer, ReviewSerializer_title_content, MovieSerializer, ReviewSerializer, ReviewSerializer_ALL

# Create your views here.
@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActorListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def actor_detail(request, movie_pk):
    actor = Actor.objects.get(pk=movie_pk)
    if request.method == 'GET':
        serializer = ActorListSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ActorListSerializer(actor, data = request.data)
        # serializer = ArticleListSerializer(instance=article, data=request.data)    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


        
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer_title_content(reviews, many=True)
    return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def review_detail(request, review_pk):
#     review = Review.objects.filter(pk = review_pk)
#     if request.
#     serializer = ReviewSerializer(review, many=True)
#     return Response(serializer.data)
'''
ReviewSerializer 새로 만들기
'''
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer_ALL(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # review = serializers.serialize("json", [Review.objects.get(pk=review_pk)])
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)