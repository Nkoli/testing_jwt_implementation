from rest_framework import serializers
from .models import Puppy

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('id', 'name', 'age', 'breed', 'colour', 'created_at', 'updated_at')
