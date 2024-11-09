from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.TextField()
    author = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "books"
