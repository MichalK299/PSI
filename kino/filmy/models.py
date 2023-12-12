from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=255)
    opis = models.TextField()
    rok_produkcji = models.IntegerField()
    rezyser = models.CharField(max_length=255)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tytul
