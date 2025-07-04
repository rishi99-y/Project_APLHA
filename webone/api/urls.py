from django.urls import path,include
from . import views


urlpatterns = [
    path('student/', views.studentView),
    path('student/<int:pk>/',views.studentdetailview)
]