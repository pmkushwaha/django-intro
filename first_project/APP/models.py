from django.db import models

 

class Author(models.Model):
    name = models.CharField(max_length=100)
    auther_id=models.IntegerField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


