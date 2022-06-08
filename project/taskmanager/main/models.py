from django.db import models


class Locomotive(models.Model):
    name_loc = models.CharField('Название:', max_length=50)
    type_loc = models.CharField('Тип:', max_length=50)
    function_loc = models.CharField('Назначение:', max_length=50)
    year = models.IntegerField('Год выпуска, год:')
    country_loc = models.CharField('Страна изготовитель:', max_length=50)
    construction_speed = models.IntegerField('Конструкционная скорость, км/ч:', max_length=50)
    weight_loc = models.IntegerField('Масса, т:', max_length=50)
    length_loc = models.IntegerField('Длина, мм:', max_length=50)
    description = models.TextField('Описание:')

    def __str__(self):
        return self.name_loc

    class Meta:
        verbose_name = 'Локомотив'
        verbose_name_plural = 'Локомотивы'
