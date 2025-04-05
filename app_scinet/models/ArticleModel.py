from django.db import models

class Article(models.Model):
    objects = None
    title = models.CharField(max_length=200)  # Pole tekstowe do 200 znaków
    content = models.TextField()  # Pole do przechowywania większego tekstu


    def __str__(self):
        return self.title