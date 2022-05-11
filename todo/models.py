from django.core.validators import MinValueValidator
from django.db import models
from datetime import date


class TODOItem(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='todo_list',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(
        validators=[MinValueValidator(date.today)],
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'TODO Item'
        verbose_name_plural = 'TODO Items'