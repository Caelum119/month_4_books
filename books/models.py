from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator 


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

    def average_rating(self):  
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum([r.mark for r in reviews]) / reviews.count(), 2)
        return None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Книги'




class Review(models.Model):
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name='выберите книгу')
    text = models.TextField(verbose_name='напишите отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Оценка должна быть от 1 до 5"),
            MaxValueValidator(5, message="Оценка должна быть от 1 до 5")
        ]
    )

    def __str__(self):
        return f"{self.choice_book} - {self.author.username}"




