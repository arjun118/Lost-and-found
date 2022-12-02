from django.urls import path
from .views import ArticleLostListView,ArticleFoundListView,  ArticleDetailView , ArticleUpdateView , ArticleDeleteView, ArticleCreateView


urlpatterns =[
    path("<int:pk>/",ArticleDetailView.as_view(),name="article_detail"),
    path("<int:pk>/edit/",ArticleUpdateView.as_view(),name="article_edit"),
    path("<int:pk>/delete/",ArticleDeleteView.as_view(),name="article_delete"),
    path("new/",ArticleCreateView.as_view(),name="article_new"),
    path("lost/",ArticleLostListView.as_view(),name="lost"),
    path("found/",ArticleFoundListView.as_view(),name="found"),
]