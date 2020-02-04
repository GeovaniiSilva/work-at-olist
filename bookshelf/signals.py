from bookshelf.models import UploadCsv
from bookshelf.serializers import AuthorSerializer
from rest_framework.response import Response
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import pandas as pd
import os


@receiver(pre_save, sender=UploadCsv)
def remove_uploaded_csv(sender, instance, **kwargs):
    uploaded = UploadCsv.objects.first()
    if uploaded:
        os.remove(uploaded.file.path)
        uploaded.delete()



@receiver(post_save, sender=UploadCsv)
def save_data_from_csv(sender, instance, **kwargs):
    if instance.file.path.endswith('.csv'):
        try:
            df = pd.read_csv(instance.file.path)
            for author in df.values:
                data = {'name':"".join(author)}
                serializer = AuthorSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
        except:
            return Response({'msg': 'Problem reading the file'})
    else:
        return Response({'msg': 'File cannot be uploaded'})
            

