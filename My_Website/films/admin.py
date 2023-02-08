from django.contrib import admin
from .models import Film, Direction, Genre, Reviews

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publ')
    list_filter = ('genre', 'date_publ')
    search_fields = ('title', )


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'film')
    readonly_fields = ('name', 'email', )
