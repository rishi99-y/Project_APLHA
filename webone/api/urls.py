from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeViewset, basename= 'employee')



urlpatterns = [
    path('student/', views.studentView),
    path('student/<int:pk>/',views.studentdetailview),
    
   
    path('', include(router.urls)),

    path('blogs/',views.blogview.as_view()),
    path('comment/',views.commentview.as_view()),

    path('blogs/<int:pk>/',views.blogdetailview.as_view()),
    path('comment/<int:pk>/',views.commentdetailview.as_view()),

]