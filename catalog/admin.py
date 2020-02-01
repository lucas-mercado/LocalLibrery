from django.contrib import admin
from .models import Book, Author, Genre, BookInstance, Language
# Register your models here.

#Interfaz por defecto.
#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)
admin.site.register(Genre)
#####personalizar la interface del admin de django.
# Los nombres de campos a ser desplegados en la lista están
# declarados en una tupla en el orden requerido

class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    #formulario de ingreso
    fields = ['first_name', 'last_name', ('data_of_birth', 'data_of_death')]
    #lista de muestra
    list_display = ('last_name', 'first_name', 'data_of_birth', 'data_of_death')
    #lista que pertenecen a este autor
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

#como es una relacion de many a many el genero
#hay que hacer una funcion.


#Puedes añadir la información de BookInstance dentro de nuestro detalle de Book
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


admin.site.register(Book, AdminBook)
#filtros para la vista.


class AdminBookInstance(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'id','due_back')
    # Cada sección tiene su propio título
    fieldsets = (
        ('Book', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(BookInstance,AdminBookInstance)
admin.site.register(Language)