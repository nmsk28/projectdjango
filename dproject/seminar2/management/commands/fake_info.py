from django.core.management.base import BaseCommand
from seminar2.models import Author, Article

class Command(BaseCommand):
    help = "Generate fake authors and article."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'name{i}', lastname=f'lastname{i}',email=f'mail{i}@mail.ru', biography=f'biography{i}',
                            birthday=f'2023-10-01')
            author.save()
            for j in range(1, count + 1):
                article = Article(title=f'Title{j}', content=f'content {j}', author_id=author, category=f'category{j}')
                article.save()
