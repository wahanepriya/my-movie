from django.contrib import admin

# Register your models here.

from movie_app.models import MovieGenre, Movies

admin.site.register(MovieGenre)
admin.site.register(Movies)
