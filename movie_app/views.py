from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from movie_app.models import Movies
from movie_app.serializers import MoviesSerializers, MoviesRetrieveSerializers
from utils.permissions import AdminOnlyPermission


class MoviesCreateView(generics.ListCreateAPIView):
    serializer_class = MoviesSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('imdb_score','director','popularity_99','name','genre__name')

    permission_classes = [AdminOnlyPermission ,]

    def get_queryset(self):
        return Movies.objects.all()


    ### By using APIView ###
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     if request.auth.user.username =='admin':
    #         if data:
    #             movie = Movies.objects.create(
    #                 imdb_score = data['imdb_score'],
    #                 director= data['director'],
    #                 popularity_99 = data['99popularity'],
    #                 name = data['name']
    #
    #             )
    #             if data['genre']:
    #                 for g in data['genre']:
    #                     movie.genre.add(g)
    #             movie.save()
    #             return Response({"status":"Movie added successfully"})
    #     else:
    #         return Response({"status":"Not allow to create movie."})


class MovieRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSerializers
    permission_classes = [AdminOnlyPermission, ]

    def get_object(self):
        queryset = self.get_queryset()
        try:
            return queryset.get(
                pk=self.kwargs['movie_id']
            )
        except queryset.model.DoesNotExist:
            pass

    def get_queryset(self):
        return Movies.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()

        serializer =  self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"status":"Movie deleted."})


class MovieRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MoviesRetrieveSerializers
    queryset = Movies.objects.all()

    def get_object(self):
        queryset = self.get_queryset()

        try:
            return queryset.get(
                pk=self.kwargs['movie_id']
            )
        except:
            pass

        raise Http404


class MovieListAPIView(generics.ListAPIView):
    serializer_class = MoviesSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('imdb_score', 'director', 'popularity_99', 'name', 'genre__name')

    def get_queryset(self):
        return Movies.objects.all()



