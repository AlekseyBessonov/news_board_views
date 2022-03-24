from django.urls import path
from .views import NewsList, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, List  # импортируем наше представление

urlpatterns = [
        path('', List.as_view()),
        path('search/', NewsList.as_view()),
        path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
        path('create/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
        path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
        path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),  # Ссылка на создание товара# Ссылка на создание товара
    ]