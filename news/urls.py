from django.urls import path
from .views import NewsListView, NewsDetailView, NewsByCategoryView
from .views import LiveNewsView


urlpatterns = [
     path('live/', LiveNewsView.as_view(), name='live-news'),
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('category/<str:category>/', NewsByCategoryView.as_view(), name='news-category'),
]