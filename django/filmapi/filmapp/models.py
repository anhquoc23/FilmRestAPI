import uuid

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


# Create your models here.

# Base Model
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=255, unique=True, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

# Model
class User(AbstractUser):
    phone_number = models.CharField(null=False, max_length=15)
    avatar = CloudinaryField('avatar', folder ='film/user/avatar', null=True)

    # Many To Many
    films = models.ManyToManyField('Film', related_name='user_films', through='History')

class Category(BaseModel):

    class Meta:
        ordering = ['name']

class Country(BaseModel):
    class Meta:
        ordering = ['name']

class Actor(BaseModel):
    birthday = models.DateField(null=True)
    avatar = CloudinaryField('avatar', folder ='film/actor/avatar', null=True, blank=True)

    #Many To Many
    films = models.ManyToManyField('Film', related_name='actors', null=True)

class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    poster = CloudinaryField('poster', folder='film/film/poster')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    duration = models.TimeField(null=False)
    numbers_episodes = models.IntegerField(null=True)
    views = models.IntegerField(default=0, editable=False)
    status = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)

    # Many To Many
    users = models.ManyToManyField('User', related_name='comments', through='Comment')
    categories = models.ManyToManyField(Category, related_name='film_category')
    countries = models.ManyToManyField(Country, related_name='film_country')
    # history = models.ManyToManyField('User', related_name='history', through='History')

    def __str__(self):
        return self.name

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     self.slug = slugify(self.name)
    #     if update_fields is not None and 'name' in update_fields:
    #         update_fields = {"slug"}.union(update_fields)
    #         super().save(force_insert, force_update, using, update_fields)


class Episode(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(unique=True, max_length=255)
    video_url = models.FileField(upload_to='video/%s' % name, null=False)

    # Many To One
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='episodes')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        if update_fields is not None and 'name' in update_fields:
            update_fields = {"slug"}.union(update_fields)
            super().save(force_insert, force_update, using, update_fields)


class History(models.Model):
    date_view = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    #Many To One
    user = models.ForeignKey(User, related_name='history', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, related_name='user_history', on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(null=False)
    is_edit = models.BooleanField(default=False)
    created_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Many To One
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    films = models.ForeignKey(Film, related_name='film_comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.content