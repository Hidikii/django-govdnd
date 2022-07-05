from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    return render(request, 'homepage/home.html')

def all_blogs(request):
    Blogs = Blog.objects.order_by('-date') # последние посты 5 последних
    return render(request, 'blog/all_blogs.html', {'blogs' : Blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # получение нужного блога в виде страницы
    return render(request, 'blog/detail.html', {'blog':blog})
