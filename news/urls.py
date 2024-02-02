from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import news_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('haberler/<slug:news_slug>/', news_detail, name='news_detail'),
    path('page/', views.page, name='page'),
    path('spor/', views.sport, name='sport'),
    path('ekonomi/', views.economy, name='economy'),
    path('magazin/', views.magazine, name='magazine'),
    path('dunya/', views.world, name='world'),
    path('contact/', views.contact, name='contact'),
    path('error/', views.error, name='error'),
    path('index2/', views.index2, name='index2'),
    path('search/', views.search, name='search'),
    path('single/', views.single, name='single'),
    path('single2/', views.single, name='single2'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)