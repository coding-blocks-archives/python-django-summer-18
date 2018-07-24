from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('books/', views.BookList.as_view(), name = 'books'),
    path('book/<int:pk>', views.BookDetail.as_view(), name = 'book'),
    path('authors/', views.AuthorList.as_view(), name = 'authors'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name = 'author'),
    path('addAuthor/', views.CreateAuthor.as_view(), name = 'addAuthor'),
    path('updateAuthor/<int:pk>', views.UpdateAuthor.as_view(), name = 'updateAuthor'),
    path('publishers/', views.PublisherList.as_view(), name = 'publishers'),
    path('publisher/<int:pk>', views.PublisherDetail.as_view(), name = 'publisher'),

    path('books/<publisher>', views.PublisherBooksList.as_view(), name = 'publisher_book_list'),

    path('success/', views.SuccessView.as_view(), name = 'success'),
]