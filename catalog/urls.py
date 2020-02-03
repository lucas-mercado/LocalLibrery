from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name='index'),]

#lista libros
urlpatterns += [url(r'^book/$', views.BookListView.as_view(), name='books'),]
#urlpatterns += [url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),]

#lista autor
urlpatterns += [url(r'^author/$', views.AuthorListView.as_view(), name='authors'), ]
urlpatterns += [url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'), ]

#ingresar author
urlpatterns += [url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'), ]

#ingresar book
urlpatterns += [url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'), ]