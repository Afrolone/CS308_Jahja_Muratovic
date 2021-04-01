from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=25)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=25)
    publication_date = models.DateTimeField('publication date')
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title