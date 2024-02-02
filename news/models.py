from autoslug import AutoSlugField
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField(default='')
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"

class Sport(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField(default='')
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Spor"
        verbose_name_plural = "Spor"

class Economy(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ekonomi"
        verbose_name_plural = "Ekonomi"

class Magazine(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Magazin"
        verbose_name_plural = "Magazin"

class World(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Dünya"
        verbose_name_plural = "Dünya"

class Technology(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Teknoloji"
        verbose_name_plural = "Teknoloji"

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Ad')
    last_name = models.CharField(max_length=100, verbose_name='Soyad')
    email = models.EmailField(verbose_name='E-posta')
    urgency = models.CharField(max_length=20, choices=[('Low', 'Düşük'), ('Medium', 'Orta'), ('High', 'Yüksek')], verbose_name='Aciliyet')
    message = models.TextField(verbose_name='Mesaj')
    agree_to_terms = models.BooleanField(default=False, verbose_name='Kullanım Koşulları\'nı Kabul Ediyorum')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'