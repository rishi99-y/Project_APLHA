from rest_framework import serializers
from student.models import students

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'