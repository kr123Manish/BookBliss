from rest_framework import serializers
from LIB_API.models import BookData

class book_Serializer(serializers.ModelSerializer):
    class Meta:
        model= BookData
        fields= '__all__'
        