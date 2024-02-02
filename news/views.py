from django.shortcuts import get_object_or_404, render
from .models import News, Sport, Economy, Magazine, World

def index(request):
    all_news = News.objects.all()
    return render(request, 'pages/index.html', {'all_news': all_news})

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    return render(request, 'pages/page.html', {'news': news})

def page(request):
    return render(request, 'pages/page.html')

def sport(request):
    all_sport = Sport.objects.all()
    return render(request, 'pages/sport.html', {'all_sport': all_sport})

def economy(request):
    all_economy = Economy.objects.all()
    return render(request, 'pages/economy.html', {'all_economy': all_economy})

def magazine(request):
    all_magazine = Magazine.objects.all()
    return render(request, 'pages/magazine.html', {'all_magazine':all_magazine})

def world(request):
    all_world = World.objects.all()
    return render(request, 'pages/world.html', {'all_world':all_world})

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
