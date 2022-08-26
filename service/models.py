from tkinter import CASCADE
from turtle import title
from django.db import models

class Post(models.Model):

    title = models.CharField(verbose_name='название', max_length=100)
    descriptions = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):

    descriptions = models.TextField(verbose_name='описание', null=True, blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.descriptions}'