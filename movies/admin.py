from django.contrib import admin

# Register your models here.
from movies.models import Person, Movie


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

class MovieInline(admin.TabularInline):
    model = Movie.actors.through

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieInline, ]