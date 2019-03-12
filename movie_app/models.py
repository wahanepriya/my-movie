import uuid

from django.db import models

# Create your models here.
from django.utils import timezone


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class UpdatedAtBaseModel(models.Model):
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.updated_at = timezone.now()
        return super(UpdatedAtBaseModel, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )


class CreatedAtBaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class DateBaseModel(BaseModel, UpdatedAtBaseModel, CreatedAtBaseModel):
    class Meta:
        abstract = True


class MovieGenre(DateBaseModel):
    name = models.CharField(max_length=140, blank=True, null=True)


class Movies(DateBaseModel):
    name = models.CharField(max_length=140, blank=True, null=True)
    popularity_99 = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    director = models.CharField(max_length=100, blank=True, null=True)
    genre = models.ManyToManyField(MovieGenre, related_name='get_movie_genre',blank=True, null=True)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=2, default=10)

    def get_all_movie_genre(self):
        return self.genre.all()


