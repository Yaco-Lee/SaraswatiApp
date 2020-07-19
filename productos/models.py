from django.db import models

class Caja_Armonizadora(models.Model):
    id = models.IntegerField(primary_key=True)
    Size = models.TextChoices('Size', 'Chico Mediano Grande')
    Note = models.TextChoices('Note', 'A B C D E F G')
    Tuning = models.TextChoices('Tuning', '432Hz 440Hz 442Hz')
    price = models.DecimalField()
