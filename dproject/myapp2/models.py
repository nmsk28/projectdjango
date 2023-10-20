from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography =
    birthday =


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Title is {self.title}'