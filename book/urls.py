from django.urls import  path

from book.views import MyAPIView, BookListView, BookDetailView


urlpatterns = [
    #path('', views.books_list, name="books_list"),
    #path('<int:pk>/', views.book_detail, name='books_detail'),
    path('', BookListView.as_view(), name='books_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='books_detail'),
    path('myview/', MyAPIView.as_view(), name='my-view'),
]