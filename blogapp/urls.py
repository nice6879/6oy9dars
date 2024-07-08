from django.urls import path
from .views import news,news_detail


urlpatterns = [
    path('',news,name='news'),
    path('detail/<int:id>/',news_detail,name='news_detail')
]

