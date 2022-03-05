from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=123)
    author = models.TextField(max_length=33)
    publish_date = models.DateTimeField('Date Published')