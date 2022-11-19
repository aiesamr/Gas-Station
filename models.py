from django.db import models

class Funcionario (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    capacidade_tanque = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.descricao

class Bomba(models.Model):
    tipo_combustivel = models.CharField(max_length=100)
    qtdd_estoque = models.IntegerField()
    capacidade = models.IntegerField()

    def __str__(self):
        return self.tipo_combustivel

class Abastecimento(models.Model):
    datAbastecimento = models.DateField(null=False, blank=False)
    qtd_litro = models.IntegerField(null=False, blank=False)
    km_odometro = models.IntegerField(null=False, blank=False)
    nomeFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeFuncionario

class CompraCombustivel(models.Model):
    dataCompra = models.DateField(null=False, blank=False)
    qtdd_litros = models.IntegerField()
    preco_litro = models.DecimalField(max_digits=5, decimal_places=2)
        
    def __str__(self):
        return self.dataCompra