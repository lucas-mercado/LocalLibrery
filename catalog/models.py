import uuid
from django.db import models
from django.urls import reverse


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Ingrese el idioma del Libro")

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    sumary = models.TextField(max_length=200)
    imprint = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=20)
    genre = models.ManyToManyField(Genre, help_text="Seleccione el Genero")
    lenguage = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    data_of_birth = models.DateField(null=True, blank=True, help_text='Ingrese fecha de nacimiento')
    data_of_death = models.DateField(null=True, blank=True, help_text='Ingrese fecha de su muerte')

    def __str__(self):
        # self.data_of_birth, self.data_of_birth
        return '%s, %s' %(self.last_name, self.first_name)


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=20)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Load'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True , default='m',help_text='Disponibilidad del libro')

    def __srt__(self):
        return  '%s (%s)' %(self.id, self.book.title)