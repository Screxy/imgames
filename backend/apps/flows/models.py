from django.db import models
from organizations.models import Organization
from django.core.validators import MaxValueValidator, MinValueValidator

MATH_OPERATOR_SELECTION = [
    ('+', '[+] Сложение'),
    ('-', '[-] Вычиатение'),
    ('*', '[*] Умножение'),
    ('/', '[/] Деление'),
]

CHANGE_TYPES_SELECTION = [
    ('FSVL', 'Изменение начального значения'),
    ('AVCH', 'Изменение среднего чека'),
    ('CONV', 'Изменение конверсии'),
]


class ParameterChange(models.Model):
    """Изменение параметра"""
    card = models.ForeignKey(
        "Card", verbose_name="Принадлежность к карточке", on_delete=models.CASCADE)
    channel = models.ForeignKey(
        "Channel", verbose_name="Изменяемый канал", on_delete=models.CASCADE)
    stage = models.ForeignKey(
        "Stage", verbose_name="Изменяемый этап", on_delete=models.CASCADE)
    math_operator = models.CharField(
        verbose_name="Математический оператор", max_length=1, choices=MATH_OPERATOR_SELECTION)
    value = models.DecimalField(
        "Дельта (изменяемое значение)", decimal_places=2, max_digits=10)
    month_of_application = models.PositiveIntegerField(
        "На какой месяц применять")
    type = models.CharField(
        verbose_name="Тип изменений", max_length=4, choices=CHANGE_TYPES_SELECTION)

    class Meta:
        verbose_name = "Изменение параметра"
        verbose_name_plural = "Изменения параметров"

    def __str__(self):
        return "Изменение параметра #"+str(self.id)


class Stage(models.Model):
    """Этап"""
    flow = models.ForeignKey("Flow", verbose_name="Принадлежность к механике",
                             on_delete=models.CASCADE)
    name = models.CharField("Название этапа", max_length=255)
    conversion = models.DecimalField(
        "Начальная конверсия", decimal_places=2, max_digits=5, validators=[
            MaxValueValidator(100.00),
            MinValueValidator(0.01)
        ])

    class Meta:
        verbose_name = "Этап"
        verbose_name_plural = "Этапы"

    def __str__(self):
        return "'"+self.name+"'"+" (#"+str(self.id)+")"


class StageInSequence(models.Model):
    """Место в последовательности этапов"""
    stage = models.OneToOneField(
        "Stage", verbose_name="Изменяемый этап", on_delete=models.CASCADE)
    place = models.PositiveIntegerField("Место")

    class Meta:
        verbose_name = "Место в последовательности этапов"
        verbose_name_plural = "Места в последовательности этапов"

    def __str__(self):
        return "(#"+str(self.id)+")"


class Channel(models.Model):
    """Канал"""
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
    cost = models.PositiveIntegerField(
        "Стоимость")

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
