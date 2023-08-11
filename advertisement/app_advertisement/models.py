from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField(
        max_length=80,
        verbose_name="Название",

    )
    description = models.TextField(
        verbose_name="Описание"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    auction = models.BooleanField(
        verbose_name="Торг",
        default=False
    )
    created_at = models.DateTimeField(
       auto_now_add=True,
        verbose_name="Дата публикации"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    @admin.display(description="Текущая дата")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S:")
    @admin.display(description="Дата изменения")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S:")

    def __str__(self):
        return f"id={self.id} title={self.title} price={self.price}"
    class Meta:
        db_table = "advertisement"