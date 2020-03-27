from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Car(models.Model):

    MECHANIC = 1
    AUTOMATIC = 2
    ROBOTIC = 3

    GEARBOX_CHOICES = [
        (MECHANIC, "механика"),
        (AUTOMATIC, "автомат"),
        (ROBOTIC, "робот"),
    ]

    manufacturer = models.CharField(
        verbose_name = u"Производитель",
        max_length=30
        )
    model = models.CharField(
        verbose_name = u"Модель",
        max_length=30
        )
    release_year = models.IntegerField(
        verbose_name = u"Год выпуска",
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2020)
            ]
        )
    gearbox = models.SmallIntegerField(
        verbose_name = u"Коробка передач",
        choices=GEARBOX_CHOICES,
        default=0
        )
    color = models.CharField(
        verbose_name = u"Цвет",
        max_length=30,
        )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='photos',
        blank=True
        )

    class Meta:
        verbose_name = u"Автомобиль"
        verbose_name_plural = u"Автомобили"

    def __str__(self):
        return f'{self.manufacturer} {self.model}'

