from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

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
