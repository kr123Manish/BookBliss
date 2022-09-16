from rest_framework import serializers
from LIB_API.models import AdminData

class signUp_Serializer(serializers.ModelSerializer):
    class Meta:
        model= AdminData
        # fields= ('admin_name', 'admin_email','admin_password')
        fields= '__all__'
        