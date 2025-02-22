from django.shortcuts import render
from rest_framework import generics
from .models import BookPost
from .serializers import BookPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookPostListCreate(generics.ListCreateAPIView):
    queryset = BookPost.objects.all()
    serializer_class = BookPostSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            'message': 'Book post created successfully',
            'data': response.data
        }
        return response
    
class BookPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookPost.objects.all()
    serializer_class = BookPostSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data = {
            'message': 'Book post updated successfully',
            'data': response.data
        }
        return response
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Book post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class BookPostSearch(APIView):
    def get(self, request, format=None):
        #Get the title from the query parameters(if none, default to empty string)
        title = request.query_params.get("title", "")

        if title:
            #filter the queryset based on title
            book_posts = BookPost.objects.filter(title__icontains=title)
            message = f"Found {book_posts.count()} book(s) matching the title '{title}'"
        else:
            #iff no title is provided, return all book posts
            book_posts = BookPost.objects.all()
            message = "Returning all book posts"
        
        serializer = BookPostSerializer(book_posts, many=True)
        return Response({
            'message': message,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
# Create your views here.
