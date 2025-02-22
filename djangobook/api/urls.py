from django.urls import path 
from . import views

urlpatterns = [
    path("bookpost/", views.BookPostListCreate.as_view(), name="bookpost-view-create"),
    path("bookpost/<int:pk>/", 
    views.BookPostRetrieveUpdateDestroy.as_view(),
    name="update",
    ),
    path("bookpost/search/", views.BookPostSearch.as_view(), name="bookpost-search"),
]

#class based view: Anytime we go to bookpost/, we are redirected to the views.
