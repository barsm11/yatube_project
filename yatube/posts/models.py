from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Название группы:',
        help_text='max 30 символов'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Уникальный адрес группы:',
        help_text='max 100 символов'
    )
    description = models.TextField(
        verbose_name='Описание сообщества:'
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста:'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации:'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор:'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='users',
        blank=True,
        null=True,
        verbose_name='Относится к группе:'
    )

    class Meta:
        unique_together = (
            'author',
            'group'
        )

# Create your models here.
