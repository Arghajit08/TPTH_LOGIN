from django.db.models import fields
from rest_framework import serializers
from .models import Register,Photo

#Created modelSerializer for each user

class UploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'