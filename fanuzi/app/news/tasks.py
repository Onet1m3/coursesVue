from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.schedules import crontab
from app.news.models import NewsModel


@shared_task
def check_news():
    print("Hello world")
    return "world"


#TODO написать парсер новостных rss лент, запускать каждую ночь и записывать новые новости в таблицу news