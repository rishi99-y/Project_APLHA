from rest_framework import serializers
from .models import blogs, comment


class commentserializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'

class blogserializer(serializers.ModelSerializer):
    comments = commentserializer(many = True, read_only = True)
    class Meta:
        model = blogs
        fields = '__all__'

