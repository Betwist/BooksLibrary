from django.core.validators import RegexValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')
    publication_year = models.IntegerField(verbose_name='Год издания')

    isbn = models.CharField(
        max_length=17,
        validators=[RegexValidator(
            regex=r'^\d{3}-\d-\d{3,5}-\d{5,7}-\d$', message='ISBN должен иметь формат 978-5-699-12014-7'
        )],
        unique=True,
        verbose_name='ISBN'
    )

    def __str__(self):
        return self.title
