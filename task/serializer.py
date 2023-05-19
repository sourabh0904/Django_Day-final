from rest_framework import serializers

class CategorySerializer(serializers.Serializer) : 
    id = serializers.UUIDField()
    name = serializers.CharFiled()
    description = serializers.CharField()
    status = serializers.BooleanField()

    class Meta : 
        fields =[
            'id',
            'name',
            'description',
            'status'
        ]
