from rest_framework import serializers
from .models import YourModelName

class YourModelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModelName
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'name', 'description']