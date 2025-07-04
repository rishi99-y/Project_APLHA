#from django.shortcuts import render
#from django.http import JsonResponse
from student.models import students
from .serializers import studentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
   if request.method == 'GET':
      #get all student
      student = students.objects.all()
      serializers = studentSerializers(student ,many = True)
      return Response(serializers.data ,status = status.HTTP_200_OK)
   elif request.method == 'POST':
      #accpet all student
        serializers = studentSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data , status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)
   #elif request.method == 'PUT':
   #   serializers = 


@api_view(['GET', 'PUT', 'DELETE'])
def studentdetailview(request,pk):
   try:
      student = students.objects.get(pk = pk)
   except students.DoesNotExist:
       return Response (status= status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
       serializers = studentSerializers(student)
       return Response (serializers.data , status= status.HTTP_302_FOUND)
   elif request.method == 'PUT':
      serializers = studentSerializers(student, data = request.data)
      if serializers.is_valid(): 
         serializers.save()
         return Response (serializers.data , status= status.HTTP_200_OK) 
      else:
          return Response (status= status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
       student.delete()
       return Response (status= status.HTTP_410_GONE)