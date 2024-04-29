from django.urls import path
from .views import *

app_name = 'edu'

urlpatterns = [
    path('models/', EduModelAPIView.as_view()),
    path('models/<int:pk>/', EduModelDetailAPIView.as_view()),
    path('models/create/', EduModelCreateAPIView.as_view()),
    path('models/delete/<int:pk>/', EduModelDetailAPIView.as_view()),
    path('models/update/<int:pk>/', EduModelDetailAPIView.as_view()),
]
