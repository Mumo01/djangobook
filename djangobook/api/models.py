from django.db import models
from .validators import validate_publication_date

# Create your models here.
class BookPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(validators=[validate_publication_date]) #Apply validation check
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField(max_length=100)

    def __str__(self):
         return f"{self.title} by {self.author} ({self.publication_date.year})"
    