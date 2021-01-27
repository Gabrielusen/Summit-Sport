from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import News


class IndexView(ListView):
    queryset = News.objects.all()
    template_name = 'base.html'
