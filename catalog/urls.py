from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [url(r'^$', views.index, name='index'), ]

#lista libros # name => para <a href={% url 'books' %}> on click <a/>
urlpatterns += [path('book/', views.list_book, name='books'), ]
urlpatterns += [path('book/<book_id>', views.book_detail, name='book-detail'), ]

#lista autor
urlpatterns += [path('author/', views.AuthorListView.as_view(), name='authors'), ]
urlpatterns += [path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'), ]

#ingresar author
urlpatterns += [path('author/create/', views.AuthorCreate.as_view(), name='author_create'), ]

#ingresar book
urlpatterns += [path('book/create/', views.BookCreate.as_view(), name='book_create'), ]