from django.db import models


class NewsModel(models.Model):
    """Таблица новостей"""
    title = models.CharField("Заголовок", max_length=250)
    link = models.URLField("Ссылка на новость")
    date_published = models.DateTimeField("Дата публикации")
    description = models.CharField("Краткое описание", max_length=500)

    def __str__(self):
        return f"{self.title} Дата публикации: {self.date_published}"

    class Meta:
        db_table = 'news'
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['date_published']