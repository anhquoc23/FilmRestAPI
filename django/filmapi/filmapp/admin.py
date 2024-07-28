from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from  .models import User, Category, Actor, Country, Film, Episode

class FilmAdminSite(admin.AdminSite):
    site_header = 'Trang Quản Trị Website Xem Phim'
    site_title = 'Admin Site'


# Register your models here.


admin_site = FilmAdminSite(name='myadmin')

# Model Admin

# AdminInline
class CategoryInLine(admin.TabularInline):
    model = Film.categories.through
class CountryInLine(admin.StackedInline):
    model = Film.countries.through

class ActorInLine(admin.StackedInline):
    model = Film.actors.through

class ActorForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActorForms, self).__init__(*args, **kwargs)
        self.fields['films'].required = False

class EpisodeInLine(admin.StackedInline):
    model = Episode
    fk_name = 'film'

class ActorAdmin(admin.ModelAdmin):
    form = ActorForms
    readonly_fields = ['image']

    def image(self, obj):
        if obj:
            return mark_safe(
                '<img src="https://res.cloudinary.com/dhbvb6aqb/{url}" width=100 alt="avatar" />'.format(url=obj.avatar)
            )

class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'poster', 'duration', 'numbers_episodes', 'views', 'is_active']
    # readonly_fields = ['slug']
    list_filter = ['name']
    inlines = [EpisodeInLine, ActorInLine]
    prepopulated_fields = {'slug': ('name', )}

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['ava']

    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="https://res.cloudinary.com/dhbvb6aqb/{url}" width=100 alt="avatar" />'.format(url=obj.avatar)
            )

admin_site.register(Film, FilmAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Category)
admin_site.register(Actor, ActorAdmin)
admin_site.register(Country)