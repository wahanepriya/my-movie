from django.contrib import admin

# Register your models here.
from movie_app.models import MovieGenre
from user.models import AllUser


class AllUserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'is_admin'
    )

admin.site.register(AllUser, AllUserAdmin)
