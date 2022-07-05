from django.urls import path
from . import views

app_name = 'blog' # короче блять обязательная хуета, не поставил = лох... Поиск приложения

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
