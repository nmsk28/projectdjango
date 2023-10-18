from django.db import models
from collections import Counter


class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сторона: {self.is_eagle}, время: {self.create_at}'

    @staticmethod
    def counter(n: int):
        coins = Coin.objects.order_by('-create_at')[: n]
        coins_dict = {'орел': 0, 'решка': 0}
        for coin in coins:
            if coin.is_eagle == 'орел':
                coins_dict['орел'] += 1
            else:
                coins_dict['решка'] += 1
        return coins_dict


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(blank=True)
    birthday = models.DateField()

    def __str__(self):
        return f'Name: {self.name},lastname: {self.lastname}, email: {self.email}, biography: {self.biography}, birthday: {self.birthday}'


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


class Comment(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    publication_date = models.DateField(auto_now_add=True)
    change_at = models.DateField(auto_now_add=True)
