
from django.db import models

from django.urls import reverse

class Genre(models.Model):
    """жанры фильмов"""
    name = models.CharField('Название', max_length=20)
    description = models.TextField("Описание", blank=True)
    url = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Direction(models.Model):
    """Режиссеры"""
    name = models.CharField('ФИО режиссера', max_length=100)
    description = models.TextField("Биография", blank=True)
    image = models.ImageField(upload_to='image/directions%Y')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Film(models.Model):
    """сами фильмы"""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/%Y')
    descriptions = models.TextField(blank=True)
    date_publ = models.DateField('Дата публикации')
    directions = models.ManyToManyField(Direction, verbose_name='Режиссеры', related_name='film_direct')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}, {self.date_publ}'

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Reviews(models.Model):
    """отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text_reviews = models.TextField('Текст отзыва', max_length=1500)
    film = models.ForeignKey(Film, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.film}'



    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'






