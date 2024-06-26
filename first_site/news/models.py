from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anonce = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'