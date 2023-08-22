from django.db import models

class Pessoa(models.Model):
    nome = models. CharField(max_length=100)
    matricula = models.IntegerField()
    senha = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Pedido(models.Model):
    horario = models.DateTimeField(auto_now=True)
    senha = models.CharField(max_length=100, default='Default')
    formPag = models.CharField(max_length=10, default='Default')
    corpoAcadId = models.ForeignKey(to='Pessoa', on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return str(self.senha) + 'pedido'


class Cardapio(models.Model):
    dia = models.DateField()
    tipoRefeicao = models.CharField(max_length=10)
    pedidoId = models.ForeignKey(to="Pedido", on_delete=models.CASCADE, default=1)
    pratoId = models.ManyToManyRel(to='Prato', field=models.CASCADE)

    def __str__(self):
        return self.pk

class Prato(models.Model):
    nome = models.CharField(max_length=100, default="Teste")
    desc = models.CharField(max_length=1000, default="Sem desc.")

    def __str__(self) -> str:
        return self.nome