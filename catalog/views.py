from django.shortcuts import render
from .models import Book,BookInstance,Author,Genre

# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_de_generos = Genre.objects.all().count()
    num_de_libros_con_m = Book.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors
                 , 'num_de_generos':num_de_generos, 'num_de_libros_con_m':num_de_libros_con_m},
    )



