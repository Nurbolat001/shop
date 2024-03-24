from django.db import models

class Products(models.Model):
    name = models.CharField("Название продукта", max_length=100)
    Composition = models.CharField("Состав", max_length=255)
    image = models.CharField("Ссылка на фото", max_length=500)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name