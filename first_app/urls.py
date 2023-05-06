from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view(), name='category-list-create'),
]
