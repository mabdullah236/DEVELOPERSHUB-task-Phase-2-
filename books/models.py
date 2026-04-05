from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    price=models.IntegerField()
    isbn=models.CharField(unique=True, max_length=10)
    publishedDate=models.DateField()
    
    
