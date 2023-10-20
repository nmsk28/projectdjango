from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(blank=True)
    birthday = models.DateField()

    def __str__(self):
        return f'Name: {self.name},lastname: {self.lastname}, email: {self.email}, biography: {self.biography}, birthday: {self.birthday}'


    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'



