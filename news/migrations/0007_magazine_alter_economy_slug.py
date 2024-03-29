# Generated by Django 5.0.1 on 2024-02-02 16:11

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_economy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='category', unique=True)),
            ],
            options={
                'verbose_name': 'Magazin',
                'verbose_name_plural': 'Magazin',
            },
        ),
        migrations.AlterField(
            model_name='economy',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='category', unique=True),
        ),
    ]
