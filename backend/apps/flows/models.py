from django.db import models
from organizations.models import Organization

MATH_OPERATOR_SELECTION = [
    ('+', '[+] Сложение'),
    ('-', '[-] Вычиатение'),
    ('*', '[*] Умножение'),
    ('/', '[/] Деление'),
]


class ParameterChange(models.Model):
    """Изменение параметра"""
    card = models.ForeignKey(
        "Card", verbose_name="Принадлежность к карточке", on_delete=models.CASCADE)
    parameter = models.ForeignKey(
        "Parameter", verbose_name="Изменяемый параметр", on_delete=models.CASCADE)
    math_operator = models.CharField(
        verbose_name="Математический оператор", max_length=1, choices=MATH_OPERATOR_SELECTION)
    value = models.DecimalField(
        "Дельта (изменяемое значение)", decimal_places=2, max_digits=10)
    month_of_application = models.PositiveIntegerField(
        "На какой месяц применять")

    class Meta:
        verbose_name = "Изменение параметра"
        verbose_name_plural = "Изменения параметров"

    def __str__(self):
        return "Изменение параметра #"+str(self.id)


class Parameter(models.Model):
    """Параметр"""
    flow = models.ForeignKey("Flow", verbose_name="Принадлежность к механике",
                             on_delete=models.CASCADE)
    name = models.CharField("Название параметра", max_length=255)
    default_value = models.DecimalField(
        "Начальное значение", decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"

    def __str__(self):
        return "'"+self.name+"'"+" (#"+str(self.id)+")"


class Card(models.Model):
    """Карточка"""
    flow = models.ForeignKey("Flow", verbose_name="Принадлежность к механике",
                             on_delete=models.CASCADE)
    header = models.CharField("Заголовок", max_length=255)
    short_description = models.TextField("Короткое описание")

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

    def __str__(self):
        return "'"+self.header+"'"+" (#"+str(self.id)+")"


class Flow(models.Model):
    """Механика"""
    organization = models.ForeignKey(
        Organization, verbose_name="Принадлежит к организации", on_delete=models.CASCADE)
    title = models.CharField("Название механики", max_length=255)

    class Meta:
        verbose_name = "Механика"
        verbose_name_plural = "Механики"

    def __str__(self):
        return self.title+" - "+str(self.organization)+" (#"+str(self.pk)+")"
