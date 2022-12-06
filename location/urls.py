from django.urls import path
from location import views

urlpatterns = [
    path('location/', views.LocationList.as_view()),
    path('location/<int:pk>/', views.LocationDetail.as_view())
]