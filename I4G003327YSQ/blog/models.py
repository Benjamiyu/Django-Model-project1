from cgitb import text
from site import USER_SITE
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    author = models.ForeignKey(USER_SITE, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date published')
    published_date = models.DateTimeField()