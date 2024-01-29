from django.shortcuts import get_object_or_404, render
from .models import News

def index(request):
    all_news = News.objects.all()
    return render(request, 'pages/index.html', {'all_news': all_news})

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    return render(request, 'pages/page.html', {'news': news})

def page(request):
    return render(request, 'pages/page.html')

def author(request):
    return render(request, 'pages/author.html')

def contact(request):
    return render(request, 'pages/contact.html')

def error(request):
    return render(request, 'pages/404.html')

def index2(request):
    return render(request, 'pages/index-2.html')

def search(request):
    return render(request, 'pages/search.html')

def single(request):
    return render(request, 'pages/single.html')

def single2(request):
    return render(request, 'pages/single2.html')
