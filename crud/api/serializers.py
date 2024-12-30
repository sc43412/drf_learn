from rest_framework import serializers
from api.models import Student


class StudentSeralizer(serializers.Serializer):
    name = serializers.CharField(required=True)
    roll_no = serializers.IntegerField(required=True)

    def create(self,data):
        print(data)
        return Student.objects.create(**data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll_no = validated_data.get('roll_no',instance.roll_no)
        instance.save()
        return instance

