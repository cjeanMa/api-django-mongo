from django.db import models

# Create your models here.

class Publicaciones(models.Model):
    author= models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.TextField()
    pages = models.IntegerField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title