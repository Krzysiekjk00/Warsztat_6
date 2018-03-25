from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='Movie_director')
    actors = models.ManyToManyField(Person, through='Role', related_name='Movie_actor')
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Role(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    role = models.CharField(max_length=64)