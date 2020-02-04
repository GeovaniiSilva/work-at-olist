from bookshelf.models import *
from rest_framework.serializers import ModelSerializer



class UploadCsvSerializer(ModelSerializer):

    class Meta:

        model = UploadCsv
        fields = '__all__'


class AuthorSerializer(ModelSerializer):

    class Meta:

        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):

    class Meta:

        model = Book
        fields = '__all__'



