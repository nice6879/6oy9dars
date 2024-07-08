from django.shortcuts import render,get_object_or_404
from .models import News

def news(request):
    news = News.objects.all()

    context = {
        'news':news
    }

    return render(request,'news.html',context)

def news_detail(request,id):
    news = get_object_or_404(News,id=id)

    context = {
        'news':news
    }
    return render(request,'detail.html',context)