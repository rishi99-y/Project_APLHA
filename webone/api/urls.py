from django.urls import path,include
from . import views


urlpatterns = [
    path('student/', views.studentView),
    path('student/<int:pk>/',views.studentdetailview),
    #### for employee
    path('employee',views.Employees.as_view()),
    path('employee/<int:pk>/',views.Employeesdetails.as_view())
]