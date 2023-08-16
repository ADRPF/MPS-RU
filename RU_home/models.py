from django.db import models

class Pessoa(models.Model):
    nome = models. CharField(max_length=100)
    matricula = models.IntegerField()
    senha = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Pedido(models.Model):
    numPedido = models.BigAutoField(primary_key=True)
    horario = models.DateTimeField(auto_now=True)
    senha = models.CharField(max_length=100, default='Default')
    formPag = models.CharField(max_length=10)
    pedido = models.ForeignKey(to="Cardapio", on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.senha


class Cardapio(models.Model):
    dia = models.DateField()
    tipoRefeicao = models.CharField(max_length=10)
    item = models.ForeignKey(to="Prato", on_delete=models.SET_NULL, null=True)

class Prato(models.Model):
    pratoId = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.nome