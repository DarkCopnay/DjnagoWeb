from django.db import models

class Contact(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField("Почта")
    number = models.IntegerField("Номер")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"