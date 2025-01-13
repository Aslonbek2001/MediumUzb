from django.db import models
from utility.models import Utility
from users.models import User

class Article(Utility):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='articles')
    title = models.CharField(max_length=200, db_index=True, db_column='title')
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
