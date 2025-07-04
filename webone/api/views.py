from django.shortcuts import render ,get_object_or_404
#from django.http import JsonResponse
from student.models import students
from .serializers import studentSerializers,employeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins , generics, viewsets
from blogs.serializers import blogserializer, commentserializer
from blogs.models import blogs,comment
from .paginations import Custompagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter


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
   
'''
class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializers = employeeSerializer(employees, many = True)
        return Response (serializers.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = employeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class Employeesdetails(APIView):
   def get_object(self, pk):    
      try:
         return Employee.objects.get(pk = pk)
      except Employee.DoesNotExist:
         raise Http404
      
   def get(self, request ,pk):
       employee = self.get_object(pk)
       serializer = employeeSerializer(employee)
       return Response(serializer.data, status= status.HTTP_302_FOUND)
   
   def put(self, request, pk):
      employee = self.get_object(pk)
      serializer = employeeSerializer(employee, data= request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data , status= status.HTTP_200_OK)
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   def delete(self, request, pk):
      employee =  self.get_object(pk)
      employee.delete()
      return Response(status= status.HTTP_410_GONE)
''' 
'''
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
   queryset = Employee.objects.all()
   serializer_class = employeeSerializer

   def get (self, request):
       return self.list(request)
   
   def post(self, request):
       return self.create(request)
   


class Employeesdetails(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = Employee.objects.all()
   serializer_class = employeeSerializer

   def get(self, request, pk):
       return self.retrieve(request,pk)
   
   def put(self, request, pk):
       return self.update(request, pk)
   
   def delete(self, request, pk):
       return self.destroy(request, pk)
'''

'''
class Employees(generics.ListCreateAPIView):
   queryset = Employee.objects.all()
   serializer_class = employeeSerializer
   

class Employeesdetails(generics.RetrieveUpdateDestroyAPIView):
   queryset = Employee.objects.all()
   serializer_class = employeeSerializer
   lookup_field = 'pk'

'''
'''
class EmployeeViewset(viewsets.ViewSet):
    def list(self, request):
      queryset = Employee.objects.all()
      serializer = employeeSerializer(queryset, many = True)
      return Response (serializer.data, status= status.HTTP_200_OK)
    
    def create(self, request):
        Serializer = employeeSerializer(data = request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status= status.HTTP_200_OK)
        return Response (Serializer.errors)
    
    def retrieve(self, request, pk = None):
        employee = get_object_or_404(Employee, pk = pk)
        serializer = employeeSerializer(employee)
        return Response (serializer.data, status= status.HTTP_200_OK)
    
    def update(self, request, pk = None ):
        employee = get_object_or_404(Employee, pk= pk)
        serializer = employeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors)
    def delete (self, request, pk= None):
        employee = get_object_or_404(Employee, pk = pk)
        employee.delete()
        return Response(status= status.HTTP_410_GONE)

'''

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    pagination_class = Custompagination
    filterset_class = EmployeeFilter



class blogview(generics.ListCreateAPIView):
    queryset = blogs.objects.all()
    serializer_class = blogserializer
    filter_backends = [SearchFilter,OrderingFilter] 
    search_fields = ['blog_title']
    ordering_fields =['id', 'blog_title'] 

class commentview(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = commentserializer

class blogdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogs.objects.all()
    serializer_class = blogserializer
    lookup_field = 'pk'

class commentdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogs.objects.all()
    serializer_class = blogserializer
    lookup_field = 'pk'
 
