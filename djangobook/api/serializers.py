from rest_framework import serializers
from .models import BookPost

class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPost
        fields = ["id", "title", "author", "publication_date", "isbn", "summary"]

#Specify class that will take model and convert to JSON compatible data

