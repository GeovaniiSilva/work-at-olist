from django.shortcuts import render
from bookshelf.models import *
from bookshelf.serializers import *
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView



class UploadCsvCreateAPIView(CreateAPIView):

    model = UploadCsv
    serializer_class = UploadCsvSerializer



class AuthorListCreateAPIView(ListCreateAPIView):

    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()



class BookListCreateAPIView(ListCreateAPIView):

    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
