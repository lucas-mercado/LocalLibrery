from django.shortcuts import render
from .models import Book,BookInstance,Author,Genre
from django.views import generic
# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_de_generos = Genre.objects.all().count()
    num_de_libros_con_m = Book.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors
                 , 'num_de_generos':num_de_generos, 'num_de_libros_con_m':num_de_libros_con_m,
                 'num_visits': num_visits},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'  # Specify your own template name/location

    #def get_queryset(self):
        # Get 5 books containing the title war
    #    return Book.objects.filter(title__icontains='war')[:5]
    
    #Cuando se hace esto es importante seguir este patrón:
    #Primero obtener el contexto existente desde nuestra superclase.
    #Luego añadir tu nueva información de contexto.
    #Luego devolver el nuevo contexto (actualizado).
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        #context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book


def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book': book_id, }
    )


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'   # your own name for the list as a template variable
    queryset = Author.objects.all()
    template_name = 'authors/author_list.html'  # Specify your own template name/location
    
    #Cuando se hace esto es importante seguir este patrón:
    #Primero obtener el contexto existente desde nuestra superclase.
    #Luego añadir tu nueva información de contexto.
    #Luego devolver el nuevo contexto (actualizado).
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        #context['some_data'] = 'This is just some data'
        return context