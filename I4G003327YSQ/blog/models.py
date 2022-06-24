
from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name='author', on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)
    published_date = models.DateTimeField()
