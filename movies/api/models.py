from django.db import models

# Create your models here.
movies=[
    {"id":1,"name":"Spadikam","year":1996, "director":"badran","genre":"drama"},
    {"id":2,"name":"drishyam","year":2017, "director":"jithu","genre":"drama"},
    {"id":3,"name":"Spider man","year":2003, "director":"jhonson","genre":"action"},
    {"id":4,"name":"bat man","year":1999, "director":"alex","genre":"action"},
    {"id":5,"name":"ANt man","year":2001, "director":"joe","genre":"comedy"},
]

class MovieList(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)