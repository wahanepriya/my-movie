
from django.conf.urls import url, include
from django.urls import path


from movie_app import views

urlpatterns = [
    url(r'^$', views.MoviesCreateView.as_view(), name='list'),
    url(r'^list/$', views.MovieListAPIView.as_view(), name='list'),
    url(r'^movie_id/(?P<movie_id>[^/]+)/$', views.MovieRUDView.as_view(), name='movie-RUD'),
    url ( r'^(?P<movie_id>[^/]+)/$' , views.MovieRetrieveAPIView.as_view ( ) ,name='movie-retrieve' ) ,


]
