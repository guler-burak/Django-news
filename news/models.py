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