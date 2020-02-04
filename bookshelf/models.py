from django.db import models
from bookshelf.validators import validate_extension_csv


class UploadCsv(models.Model):

    file = models.FileField(upload_to='media/', validators=[validate_extension_csv])


class Author(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    name = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')

