from rest_framework import serializers
from student.models import students
from employees.models import Employee

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'