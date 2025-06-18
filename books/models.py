from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=100, verbose_name='Напишите название книги')
  image = models.ImageField(upload_to='book/', verbose_name='Загрузите картинку')
  description = models.TextField(verbose_name='Дайте описание книги')
  TYPE_BOOK = (
    ('Science', 'Science'),
    ('Fiction', 'Fiction'),
    ('Adventure', 'Adventure'),
    ('Fantasy', 'Fantasy'),
  )
  type_book = models.CharField(max_length=100, choices=TYPE_BOOK)
  created_at = models.DateTimeField(auto_now_add=True)

  audio_link = models.URLField(verbose_name='Embed-ссылка на аудиокнигу', null=True, blank=True)


  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'Book'
    verbose_name_plural = 'Книги'