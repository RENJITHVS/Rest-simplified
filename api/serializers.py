from rest_framework import serializers
from .models import Student
import re

#custom validators - high priority
def start_with_r(value):
    if value[0] == 'r':
        raise serializers.ValidationError("Name shouldn't start with r")

#same as django forms
class StudentSerializer(serializers.Serializer):
    # id  = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    #single filed validation - meduim prority
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    #object level validation - least priority
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        #check weather only space and alphabet
        if not bool(re.match('[a-zA-Z\s]+$', name)) and not bool(re.match('[a-zA-Z\s]+$', city)):
            raise serializers.ValidationError("only contain sapce and letters")
        return data


class StudentModelSeralizer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['id','name','city', 'roll']
        # read_only_fields = ['name']
        # extra_kwargs = {'name': {'read-only': True}}
