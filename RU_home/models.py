from django.db import models

class Pessoa(models.Model):
    nome = models. CharField(max_length=100)
    matricula = models.IntegerField()

    def __str__(self) -> str:
        return self.nome