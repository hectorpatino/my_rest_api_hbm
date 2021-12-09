from django.db import models


class BoredAndJoke(models.Model):
    type = models.CharField('type', max_length=50, null=False)
    actividad = models.TextField('actividad', null=False)
    key = models.PositiveIntegerField(null=False)
    chiste = models.TextField('chiste', null=False)

