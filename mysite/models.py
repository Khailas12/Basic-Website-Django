from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=123)
    publish_date = models.DateTimeField('Date Published')