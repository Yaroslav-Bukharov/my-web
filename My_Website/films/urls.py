from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmsViews.as_view(), name='home'),
    path('<slug:slug>/', views.FilmDetail.as_view(), name='film_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review')
]