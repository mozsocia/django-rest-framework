from .views import BookListCreateView
from django.urls import path
from .views import PersonListCreateView


from django.urls import path
from .views import CategoryListAPIView


urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person_list_create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    # path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(),
    #      name='book-retrieve-update-delete'),
]
