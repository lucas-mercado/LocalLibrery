from django.shortcuts import render
from .models import Book,BookInstance,Author,Genre
from django.views import generic
from django.http import Http404
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


def list_book(request):
    context = {'books': Book.objects.all()}
    return render(request, 'catalog/book_list.html', context)


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    context = {
        'book': book
    }
    return render(request, 'catalog/book_detail.html', context)

#class BookListView(generic.ListView):
#    model = Book
#    paginate_by = 10

    #variable que se va usar en la template
#    context_object_name = 'book_list'
    #consulta
#    queryset = Book.objects.all()
    #template ubicacion/nombre
#    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    
    #Cuando se hace esto es importante seguir este patrón:
    #Primero obtener el contexto existente desde nuestra superclase.
    #Luego añadir tu nueva información de contexto.
    #Luego devolver el nuevo contexto (actualizado).
#    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
#        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        #context['some_data'] = 'This is just some data'
#        return context


#class BookDetailView(generic.DetailView):
    #model = Book

    #def book_detail_view(request, book_id):
        #try:
         #   book = Book.objects.get(pk=book_id)
        #except Book.DoesNotExist:
        #    raise Http404("Book does not exist")
        #context = {'book': book,}
        #book_id=get_object_or_404(Book, pk=pk)
        #return render(
        #    request,
        #    'catalog/book_detail.html',
        #    context
        #)


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


from django.contrib.auth.mixins import LoginRequiredMixin


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDelete(DeleteView):
    model = Author
    sucess_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'

