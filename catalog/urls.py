from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

#lista libros
urlpatterns += [url(r'^book/$', views.BookListView.as_view(), name='books'),]
urlpatterns += [url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),]

#lista autor
urlpatterns += [url(r'^author/$', views.AuthorListView.as_view(), name='authors'), ]
