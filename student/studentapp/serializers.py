from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    age=serializers.IntegerField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

