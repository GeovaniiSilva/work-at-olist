from django.urls import path
from bookshelf.views import *


urlpatterns = [
    path('read-csv/', UploadCsvCreateAPIView.as_view(), name='read-csv'),
    path('authors/', AuthorListCreateAPIView.as_view(), name='list-authors'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='detail-author'),
    path('books/', BookListCreateAPIView.as_view(), name='list-books'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='detail-book'),
]