from django.urls import path

from books import views


app_name = 'books'

urlpatterns = [
    path('books/', views.BookListViewSet.as_view(), name="books")
]