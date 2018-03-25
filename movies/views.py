from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer

class MoviesView(APIView):

    def get_object(self):
        try:
            return Movie.objects.all()
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        movies = self.get_object()
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

class MovieView(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404


    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)
