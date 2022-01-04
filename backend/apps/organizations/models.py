from django.db import models

# Организация
class Organization(models.Model):
    organization_owner_id = models.ForeignKey("users.User", verbose_name="Владелец организации", on_delete=models.CASCADE)
    name = models.CharField("Название пространства", max_length=255)
    subdomain = models.CharField("Поддомен", max_length=50)
    prefix = models.CharField("Префикс комнат", max_length=10)
    created_at = models.DateTimeField("Создано в", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено в",auto_now=True)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.name

