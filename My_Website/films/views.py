from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Film
from .form import ReviewForm

class FilmsViews(View):
    """здесь список всех фильмов"""
    def get(self, request):
        films = Film.objects.all()
        return render(request, 'films/film.html', {'film_list': films})

class FilmDetail(View):
    """страница фильма"""
    def get(self, request, slug):
        film = Film.objects.get(url=slug)
        return render(request, 'films/film_detail.html', {'film': film})

class AddReview(View):
    """Добавление отзывов"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        film = Film.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.film = film
            form.save()
        return redirect(film.get_absolute_url())

